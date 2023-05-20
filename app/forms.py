from django import forms

class FormularioLogin(forms.Form):

    correo= forms.EmailField()
    password = forms.CharField()
