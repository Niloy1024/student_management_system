from django.forms import ModelForm
from django import forms
from .models import MyUser,Test


class Testform(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ['teacher']

class UserForm(ModelForm):
    class Meta:
        model =  MyUser 
        exclude = ['last_login']
    def save(self, commit=True):
        # Save the provided password in hashed format
        print('save method called ...')
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user 


    
