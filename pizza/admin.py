from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix',)  # colonnes affichées
    search_fields = ('nom', 'ingredients')  # barre de recherche
    list_filter = ('vegetarienne',)  # filtres à droite

admin.site.register(Pizza, PizzaAdmin)