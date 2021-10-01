from django.shortcuts import render

from django.http import HttpResponse
from .models import Pizza


def index(request):
    pizzas = Pizza.objects.all()
    return render(request, "pizzaCompany/index.html", {"pizzas": pizzas})
