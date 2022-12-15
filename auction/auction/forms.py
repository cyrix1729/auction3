from django.forms import ModelForm
from auctionApp.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'DOB', 'password1', 'password2', 'image']
        
form = RegisterForm()

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['image', 'username', 'email', 'DOB']
        labels = {'image': 'Profile Picture',
                  'username' : 'Username', 
                  'email':' Email',
                  'DOB': 'Date of Birth', 
                   }