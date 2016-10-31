from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cardList$', views.card_list, name='card_list'),
    url(r'^api/getCards', views.get_cards, name='get_cards'),
    url(r'^newCard', views.new_card, name='new_card'),
    url(r'^api/uploadNewCard', views.upload_new_card, name='upload_new_card'),
]
