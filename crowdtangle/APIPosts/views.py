import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from APIPosts.models import APIData
from crowdtangle.local_settings import API_KEY


def hit_api(request):
    context = {}

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
                        # if we found the item - then make updates
                        api_data = APIData.objects.get(api_id=post.get('id'))
                    except ObjectDoesNotExist:
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

        data = APIData.objects.all()
        context = {'data': data}

    else:
        data = APIData.objects.all()
        context = {'data': data}

    return render(request, 'home_page.html', context)


def delete_item(request, row_id):
    context = {}

    # if request.method == 'POST':
    try:
        delete_obj = APIData.objects.get(id=row_id)
        delete_obj.delete()
    except ObjectDoesNotExist:
        pass

    context['data'] = APIData.objects.all()

    return render(request, 'home_page.html', context)
