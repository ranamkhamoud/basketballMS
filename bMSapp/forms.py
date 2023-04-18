from django import forms
from .models import Player, Coach
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from . import models
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Enter a valid email address.')

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")


class ProfileForm(forms.ModelForm):
    ROLE_CHOICES = (
        ('P', 'Player'),
        ('C', 'Coach'),
        ('M', 'Manager'),
    )

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect,
                             required=True, initial='P', help_text='Required.')

    phone_number = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Profile
        fields = ['phone_number', 'date_of_birth']


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['profile', 'position']


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['profile']
