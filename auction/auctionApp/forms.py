from django.contrib.auth.forms import UserCreationForm
from django import forms
from auctionApp.models import User

#used to customize admin page
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


#Used for login
class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)