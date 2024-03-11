from django import forms
from .models import userForm

class userDetails(forms.ModelForm):
    class Meta:
        model = userForm
        fields = ['username', 'email', 'phonenumber']