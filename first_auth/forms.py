from django import forms
from first_auth.models import readers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class signinform(UserCreationForm):
 
    class Meta:
        model = User
        fields = ('username','password1','password2')




class registerform(forms.ModelForm):
    username = forms.CharField()

    
   
    class Meta:
        
        model = readers
        fields = ('username',)



    