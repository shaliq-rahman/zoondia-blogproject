from typing import Any
from django import forms
from blogplatfrm.models import User
import re

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200,  required=True)
    user_name = forms.CharField(max_length=25,  required=True)
    email = forms.CharField(max_length=25,required=True)
    password = forms.CharField(max_length=50,  required=True)   
    
    def clean(self):
        data = self.cleaned_data
        user_name =  data['user_name'] 
        email =  data['email'] 
        password =  data['password'] 
        
        if User.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError('A User with that user name already exists.')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A User with same email already exists.')
        
        if not validate_password(password):
            raise forms.ValidationError('Password must consist atleast 8 characters, one uppercase, one lowercase and a number')

        return data
    
    
    
class SignInForm(forms.Form):
    email = forms.CharField(max_length=25,required=True)
    password = forms.CharField(max_length=50,  required=True)   
    

def validate_password(password):
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    match = re.match(pattern, password)
    return bool(match)
            

    

    

    
    