from django.conf.urls import url

from APIPosts import views


urlpatterns = [

    url(r'^$', views.hit_api, name='hit_api'),
    # url(r'^(?P<row_id>\d+)/delete_item/$', views.delete_item, name='delete_item'),
    url(r'^delete_item/(\d+)/', views.delete_item, name='delete_item'),
    ]