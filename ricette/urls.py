from django.urls import path
from . import views

urlpatterns = [
    path('', views.ricette, name='home'),
    path('primi', views.primi, name='primi'),
    path('secondi', views.secondi, name='secondi'),
    path('contorni', views.contorni, name='contorni'),
    path('dolci', views.dolci, name='dolci'),
    path('accedi', views.accedi, name='accedi'),
    path('registrati', views.registrati, name='registrati'),
    path('search', views.search, name='search'),
    path('accesso', views.accesso, name='accesso'),
    path('accesso/preferiti', views.preferiti, name='preferiti'),
    path('accesso/aggiungi', views.aggiungi, name='aggiungi'),
    path('accesso/primi', views.primi_a, name='primi_a'),
    path('accesso/secondi', views.secondi_a, name='secondi_a'),
    path('accesso/contorni', views.contorni_a, name='contorni_a'),
    path('accesso/dolci', views.dolci_a, name='dolci_a'),
    path('accesso/search', views.search_a, name='search_a')
]
