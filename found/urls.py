from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^itemList$', views.item_list, name='found_list'),
    url(r'^api/getItems', views.get_items, name='get_items'),
    url(r'^api/getCategories', views.get_categories, name='get_categories'),
    url(r'^api/getLocations', views.get_locations, name='get_locations'),
]
