from django import forms
from .models import Player, Coach, Manager
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, timedelta



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
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[
            MinValueValidator(date(1925, 1, 1),message="DOB must be after 1925-01-01"),
            MaxValueValidator(date(2008, 1, 1),message="You must be at least 15 years old"),
        ],help_text='Must be older than 15 years old')



    class Meta:
        model = Profile
        fields = ['phone_number', 'date_of_birth']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["password", "last_login", "is_superuser", "is_staff",
                   "is_active", "date_joined", "groups", "user_permissions"]


class PlayerEditForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ["profile",'pending_payment']


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['profile']


class EventForm(forms.Form):
    summary = forms.CharField(label='Summary', max_length=100)
    location = forms.CharField(label='Location', max_length=100)
    description = forms.CharField(
        label='Description', max_length=500, widget=forms.Textarea)
    start_time = forms.DateTimeField(
        label='Start Time', widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    duration = forms.FloatField(label='Duration (hours)')
