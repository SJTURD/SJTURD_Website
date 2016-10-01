from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^items$', views.items, name='found_list'),
    url(r'^api/getLostItems', views.get_lost_items, name='get_lost_items'),
    url(r'^newLost$', views.new_lost, name='new_lost'),
    url(r'^newLost/foundList$', views.search, name='found_list'),
    url(r'^uploadLostItem', views.upload_lost_item, name='upload_lost_item'),
    url(r'^uploadResult', views.upload_result, name='upload_result')
]