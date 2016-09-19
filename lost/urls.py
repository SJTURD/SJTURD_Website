from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^items$', views.items, name='found_list'),
    url(r'^api/getLostItems', views.get_lost_items, name='get_lost_items'),
    url(r'^newLost$', views.new_lost, name='new_lost'),
    url(r'^newLost/foundList$', views.found_list, name='found_list'),
]