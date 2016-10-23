from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cardList$', views.card_list, name='card_list'),
    url(r'^api/getCards', views.get_cards, name='get_cards'),
]
