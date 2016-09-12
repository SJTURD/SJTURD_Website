from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^items$', views.items, name='found_list'),
    url(r'^api/getLostItems', views.get_lost_items, name='get_lost_items'),
    url(r'^match$', views.match, name='match'),
    url(r'^matchResult$', views.match_result, name='match_result'),
]