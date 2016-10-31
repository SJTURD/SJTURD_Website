from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/getCategories', views.get_categories, name='get_categories'),
    url(r'^api/getLocations', views.get_locations, name='get_locations'),
    url(r'^lfoffice/$',views.lfoffice, name='lfoffice'),
    url(r'^api/getLFOffices',views.get_lfoffices, name='get_lefoffices'),
]