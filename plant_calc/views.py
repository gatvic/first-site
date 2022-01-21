from django.shortcuts import render
from .form import AddPlantForm
# , SubForm
# from django.http import HttpResponse
# Create your views here.
from .models import *


def calc(request):
    names = Plant.objects.all()
    return render(request, 'calc/calc.html', {'names': names})


def add_plant(request):
    plantform = AddPlantForm()
    return render(request, 'calc/calc.html', {'form': plantform})


''''
def index_1(request):
    subform = SubForm
    return render(request, 'calc.html', {'form': subform})'''
