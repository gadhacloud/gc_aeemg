
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('enregistrer',views.ajout_Utilisateur,name='enregistrer'),
]