from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^itemList$', views.item_list, name='vol_found_list'),
    url(r'^item', views.item, name='vol_found_item'),
    url(r'^api/getItems', views.get_items, name='vol_get_found_items'),
    url(r'^api/getItem', views.get_item, name='vol_get_found_item'),

    url(r'^login/$', views.login, name="vol login view"),
    url(r'^$', views.index_init, name="vol index"),
    url(r'^upload/$', views.upload_view, name="vol upload view"),
    # url(r'^retrieve$', views.retrieve_view, name = "vol retrieve view"),
    url(r'^api/login', views.login, name="vol login"),
    # url(r'^api/upload', views.upload, name="vol upload"),
    url(r'^api/retrieve', views.retrieve, name = "vol retrieve"),
]
