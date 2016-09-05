from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^items$', views.items, name='found_list'),
]