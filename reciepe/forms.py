from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class Add_Reciepe_Form(forms.ModelForm):
    class Meta:
        model=Reciepe_Details
        exclude = ('user_name',)
        fields='__all__'
        