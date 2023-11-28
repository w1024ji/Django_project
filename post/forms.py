from django import forms

class MyForm(forms.Form):
    my_text = forms.CharField(max_length=100)