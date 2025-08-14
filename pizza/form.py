from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["nom", "ingredients", "vegetarienne", "prix"]
        widgets = {
            'nom': forms.TextInput(attrs= {
                'class' : 'input w-full',
                'placeholder' : 'Nom'
            }),
            'ingredients': forms.TextInput(attrs= {
                'class' : 'input w-full',
                'placeholder' : 'ingrédients'
            }),
            'vegetarienne': forms.CheckboxInput(),
            'prix': forms.TextInput(attrs= {
                'class' : 'input w-full',
                'placeholder' : 'prix'
            })
        }