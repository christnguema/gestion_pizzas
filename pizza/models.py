from django.db import models

# Create your models here.
class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=500)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
