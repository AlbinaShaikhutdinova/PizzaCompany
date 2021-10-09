from django.shortcuts import render

from django.http import HttpResponse
from .models import Pizza


def index(request):
    return render(request, "pizzaCompany/index.html")


def menuPage(request):
    pizzas = Pizza.objects.all()
    return render(request, "pizzaCompany/menu.html", {"pizzas": pizzas})


def cartPage(request):
    return render(request, "pizzaCompany/cart.html")


def homePage(request):
    return render(request, "pizzaCompany/home.html")



