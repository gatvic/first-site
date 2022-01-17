from django import forms
# from django.forms.widgets import Select
# from .models import *


class AddPlantForm(forms.Form):

    plant = forms.CharField(label='Растение')
    n = forms.IntegerField()
