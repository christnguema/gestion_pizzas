from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza
from .form import PizzaForm

# Create your views here.
def liste_pizzas(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza/list.html', {'pizzas' : pizzas})

def ajouter_pizza(request):
    form = PizzaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_pizzas')
    return render(request, 'pizza/form.html', {'form' : form})

def modifier_pizza(request, id):
    pizza = get_object_or_404(Pizza, id=id)
    form = PizzaForm(request.POST or None, instance=pizza)
    if form.is_valid():
        form.save()
        return redirect('liste_pizzas')
    return render(request, 'pizza/form.html', {'form' : form})

def supprimer_pizza(request, id):
    pizza = get_object_or_404(Pizza, id=id)
    if request.method == "POST":
        pizza.delete()
        return redirect('liste_pizzas')
    return render(request, 'pizza/confirm_delete.html', {'pizza' : pizza})
