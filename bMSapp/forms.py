from django import forms
from .models import Player,Coach
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from . import models


class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number', 'date_of_birth', 'is_player', 'is_coach', 'is_manager')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        is_player = cleaned_data.get('is_player')
        is_coach = cleaned_data.get('is_coach')
        is_manager = cleaned_data.get('is_manager')

        if not any([is_player, is_coach, is_manager]):
            raise forms.ValidationError("Please select at least one role (Player, Coach, or Manager).")

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match.")


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['profile', 'position', 'team']

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['profile', 'team']

class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ['username', 'password']

        labels = {
            'username': 'Username',
            'password': 'Password',
        }
