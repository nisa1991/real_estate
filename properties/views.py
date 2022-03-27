from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import Property


class ListProperties(ListView):
    model = Property
    template_name = 'list_properties.html'
