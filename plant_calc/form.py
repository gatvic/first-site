from django import forms

from .models import Plants #, Substances


class PlantForm(forms.ModelForm):

    class Meta:
        model = Plants
        fields = ['plant', 'n', 'p', 'k', 'ca', 'mg']
'''class SubForm(forms.Form):

    sub = forms.CharField()
    n = forms.IntegerField()
    p = forms.IntegerField()
    k = forms.IntegerField()
    ca = forms.IntegerField()
    mg = forms.IntegerField()'''
