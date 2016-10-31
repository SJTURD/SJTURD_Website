from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^itemList$', views.item_list, name='found_list'),
    url(r'^item', views.item, name='found_item'),
    url(r'^api/getItems', views.get_items, name='get_found_items'),
    url(r'^api/getItem', views.get_item, name='get_found_item'),
]
