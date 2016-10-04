from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.login, name="vol login view"),
    url(r'^index/$', views.index_init, name="vol index"),
    url(r'^upload/$', views.upload_view, name="vol upload view"),
    # url(r'^retrieve$', views.retrieve_view, name = "vol retrieve view"),
    url(r'^api/login', views.login, name="vol login"),
    # url(r'^api/upload', views.upload, name="vol upload"),
    url(r'^api/retrieve', views.retrieve, name = "vol retrieve"),
]
