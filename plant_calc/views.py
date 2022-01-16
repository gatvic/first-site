from django.shortcuts import render
from .form import PlantForm
# , SubForm
# from django.http import HttpResponse
# Create your views here.


def calc(request):
    return render(request, 'calc/calc.html', {})


def index(request):
    plantform = PlantForm()
    return render(request, 'calc.html', {'form': plantform})


''''
def index_1(request):
    subform = SubForm
    return render(request, 'calc.html', {'form': subform})'''
