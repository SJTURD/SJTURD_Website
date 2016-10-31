from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^beforeUpload$', views.before_upload, name='before_upload_lost'),
    url(r'^itemList$', views.item_list, name='lost_list'),
    url(r'^item', views.item, name='lost_item'),
    url(r'^api/getItems', views.get_items, name='get_lost_items'),
    url(r'^api/getItem', views.get_item, name='get_lost_item'),
    url(r'^newLost$', views.new_lost, name='new_lost'),
    url(r'^uploadLostItem', views.upload_lost_item, name='upload_lost_item'),
    url(r'^upload', views.upload, name='upload_result'),
]