from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.liste_pizzas, name="liste_pizzas"),
    path('ajouter/', views.ajouter_pizza, name="ajouter_pizza"),
    path('modifier/<int:id/>', views.modifier_pizza, name="modifier_pizza"),
    path('supprimer/<int:id>/', views.supprimer_pizza, name="supprimer_pizza"),
]