from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegisterForm(UserCreationForm):
    class Meta :
        model = User 
        fields = ('username', 'email', 'password1', 'password2', )
        labels = { 'mob': 'Mobile number', 'bio': 'bio'}

class UserUpdateForm (forms.ModelForm):
	email = forms.EmailField()

	class Meta :
		model = User 
		fields = ['username', 'email']

class ProfileUpdateForm (forms.ModelForm):
	class Meta :
		model = Profile
		fields = [ 'profile_pic', 'mobile', 'location', 'bio']
