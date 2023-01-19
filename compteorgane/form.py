from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import  User, Organe


#==============
class formUser(forms.ModelForm):
    class Meta:
        model=User
        fields=['id','membre','login','organe','motDePasse','type']
        widgets={
            'membre':forms.TextInput(attrs={'class':'form-group row'}),
            'login':forms.TextInput(attrs={'class':'form-group row'}),
            'organe':forms.TextInput(attrs={'class':'form-group row'}),
            'motDePasse':forms.PasswordInput(attrs={'class':'form-group row', 'placeholder':'mot de passe'}),
            'type':forms.TextInput(attrs={'class':'form-group row'}),
    }



#==============
class formOrgane(forms.ModelForm):
    class Meta:
        model=Organe
        fields=['id','nom']
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-group row'}),
    }
