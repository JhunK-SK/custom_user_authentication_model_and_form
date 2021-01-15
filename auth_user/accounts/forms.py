from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import CustomUser


class RegistrationForm(UserCreationForm):
    email           = forms.EmailField(max_length=60, help_text='Required, Enter avalid Email address.')
    
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']
        

class CustomUserAuthenticationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model   = CustomUser
        fields  = ['email', 'password']
        
    def clean(self):
        email       = self.cleaned_data['email']
        password    = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid login man') # this makes attributes named as non_field_errors, you can use passed 'form' + .non_field_errors
    