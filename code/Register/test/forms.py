from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm): #Creating a new class called UserForm to be called upon in views.py, I have included forms.ModelForm as the form is going to be mapped directly to the user model
    password = forms.CharField(widget=forms.PasswordInput) #Creates string field for Password, the widget argument tells Dango how to handle the HTML input. The widget deals with data from POST/GETs 

    class Meta: #This is a class sets Metadeta to the form 
        model = User #Associate our user model directly to the form
        fields = ['username', 'email', 'password'] #Express which fields can be written in by the user on the html, otherwise user could set admin rights to themselves.
