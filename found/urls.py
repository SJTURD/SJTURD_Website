from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^items$', views.items, name='found_list'),
    url(r'^api/getFoundItems', views.get_found_items, name='get_found_items'),
    url(r'^api/getCategories', views.get_categories, name='get_categories'),
    url(r'^api/getLocations', views.get_locations, name='get_locations'),
]
