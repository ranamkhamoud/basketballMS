
from django.contrib.auth.models import User, Group
from .models import *
from django.shortcuts import render, redirect


def create_notification(owner, user, message):
    notification = Notification.objects.create(
        owner=owner, profile=user, message=message)
    notification.save()


def create_profile(user_form, profile_form):
    # I'm sure there is a better way to do this (maybe kwargs? custom form?)
    username = user_form.cleaned_data['username']
    password = user_form.cleaned_data['password1']
    first_name = user_form.cleaned_data['first_name']
    last_name = user_form.cleaned_data['last_name']
    role = profile_form.cleaned_data['role']
    phone_number = profile_form.cleaned_data['phone_number']
    date_of_birth = profile_form.cleaned_data['date_of_birth']
    email = user_form.cleaned_data['email']
    user = User.objects.create_user(
        username, password=password, first_name=first_name, last_name=last_name, email=email)
    profile = Profile.objects.create(
        user=user, phone_number=phone_number, date_of_birth=date_of_birth)
    if role == 'P':

        group = Group.objects.get_or_create(name='Players')[0]
        user.groups.add(group)
        player = Player(profile=profile)
        player.save()
        create_notification(player.profile, player.profile,
                            'has joined the team!')
    elif role == 'C':
        group = Group.objects.get_or_create(name='Coaches')[0]
        user.groups.add(group)

        coach = Coach(profile=profile)
        coach.save()
    elif role == 'M':
        group = Group.objects.get_or_create(name='Managers')[0]
        user.groups.add(group)

        manager = Manager(profile=profile)
        manager.save()
    return user


def redirect_user(user):
    if user.groups.filter(name='Players').exists():
        return redirect('player_after_login')
    if user.groups.filter(name='Coaches').exists():
        return redirect('coach_after_login')
    if user.groups.filter(name='Managers').exists():
        return redirect('manager_after_login')


def is_player(user):
    return user.groups.filter(name='Players').exists()


def is_coach(user):
    return user.groups.filter(name='Coaches').exists()


def is_manager(user):
    return user.groups.filter(name='Managers').exists()


def not_player(user):
    return not is_player(user)
