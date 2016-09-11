from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^items$', views.items, name='found_list'),
    url(r'^api/getFoundItems', views.get_found_items, name='get_found_items'),
]
