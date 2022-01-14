from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_2(request):
    return HttpResponse('Здесь будет калькулятор')
