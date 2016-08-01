import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from APIPosts.models import APIData, Media, ActualStatistics, \
    ExpectedStatistics, Account
from crowdtangle.local_settings import API_KEY


def hit_api(request):

    if request.method == 'POST':
        headers = {'x-api-token': API_KEY}
        response = requests.get('https://api.crowdtangle.com/posts.json',
                                headers=headers)

        results = response.json()

        if 'result' in results.keys():
            if 'posts' in results['result'].keys():
                posts = results['result']['posts']

                for post in posts:
                    try:
                        # if we found the item - then make just update
                        api_data = APIData.objects.get(api_id=post.get('id'))
                    except ObjectDoesNotExist:
                        # if the item wasn't found - create it
                        api_data = APIData()
                        api_data.api_id = post.get('id')

                    api_data.platform = post.get('platform')
                    api_data.date = post.get('date')
                    api_data.type = post.get('type')
                    api_data.message = post.get('message')
                    api_data.expandedLinks = post.get('expandedLinks')
                    api_data.link = post.get('link')
                    api_data.postUrl = post.get('postUrl')
                    api_data.subscriberCount = post.get('subscriberCount')
                    api_data.score = post.get('score')
                    api_data.save()

                    media_list = post.get('media')
                    for item in media_list:
                        media = Media()
                        media.api_data = api_data
                        media.type = item.get('type')
                        media.url = item.get('url')
                        media.height = item.get('height')
                        media.width = item.get('width')
                        media.full = item.get('full')
                        media.save()

                    a_stats = ActualStatistics()
                    actual_dict = post.get('statistics').get('actual')
                    a_stats.likeCount = actual_dict.get('likeCount')
                    a_stats.shareCount = actual_dict.get('shareCount')
                    a_stats.commentCount = actual_dict.get('commentCount')
                    a_stats.save()
                    api_data.act_statistics = a_stats

                    e_stats = ExpectedStatistics()
                    expected_dict = post.get('statistics').get('expected')
                    e_stats.likeCount = expected_dict.get('likeCount')
                    e_stats.shareCount = expected_dict.get('shareCount')
                    e_stats.commentCount = expected_dict.get('commentCount')
                    e_stats.save()
                    api_data.exp_statistics = e_stats

                    account = Account()
                    account_dict = post.get('account')
                    account.api_id = account_dict.get('id')
                    account.name = account_dict.get('name')
                    account.handle = account_dict.get('handle')
                    account.profileImage = account_dict.get('profileImage')
                    account.subscriberCount = account_dict.get('subscriberCount')
                    account.url = account_dict.get('url')
                    account.platform = account_dict.get('platform')
                    account.verified = account_dict.get('verified')
                    account.save()
                    api_data.account = account
                    api_data.save()

    data = APIData.objects.all().order_by('date')
    context = {'data': data}

    return render(request, 'home_page.html', context)


def delete_item(request):
    context = {}

    row_id = request.POST.get('row_id')

    try:
        delete_obj = APIData.objects.get(id=row_id)
        delete_obj.delete()
    except ObjectDoesNotExist:
        pass

    context['data'] = APIData.objects.all().order_by('date')

    return render(request, 'home_page.html', context)
