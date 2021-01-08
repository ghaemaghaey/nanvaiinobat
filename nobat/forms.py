from django import forms

class MyValidationsForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    amount = forms.IntegerField()
