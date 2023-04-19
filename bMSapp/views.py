from django.shortcuts import render, redirect
from .models import Player, Coach, Manager, Profile
from .forms import CoachForm, UserForm, ProfileForm, UserEditForm, PlayerEditForm
from django.contrib.auth.models import User, Group, Permission
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from .utils import *


def whiteboard(request):
    return render(request, 'whiteboard.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect_user(user)

        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    user_form = UserForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = create_profile(user_form=user_form,
                                  profile_form=profile_form)

            login(request, user)

            return redirect_user(user)

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
@user_passes_test(is_player)
def player_after_login(request):
    current_player = Player.objects.get(profile__user=request.user)

    return render(request, 'player_after_login.html', {'player': current_player})


@login_required
@user_passes_test(is_coach)
def coach_after_login(request):
    current_coach = Coach.objects.get(profile__user=request.user)
    players = Player.objects.all()
    return render(request, 'coach_after_login.html', {'coach': current_coach, 'players': players})


@login_required
@user_passes_test(is_manager)
def manager_after_login(request):

    current_manager = Manager.objects.get(profile__user=request.user)

    all_players = Player.objects.all()
    all_coaches = Coach.objects.all()

    return render(request, 'manager_after_login.html', {'manager': current_manager, 'players': all_players, 'coaches': all_coaches})


@login_required
@user_passes_test(not_player)
def edit_player_profile(request, username):
    player = Player.objects.get(profile__user__username=username)
    player_form = PlayerEditForm(instance=player)
    user_form = UserEditForm(instance=player.profile.user)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=player.profile.user)
        player_form = PlayerEditForm(request.POST, instance=player)
        if player_form.is_valid() and user_form.is_valid():
            player_form.save()
            user_form.save()
            return redirect_user(request.user)
    return render(request, 'edit_profile.html', {'player_form': player_form, 'form': user_form})


@login_required
@user_passes_test(is_manager)
def edit_coach_profile(request, username):
    coach = Coach.objects.get(profile__user__username=username)
    user_form = UserEditForm(instance=coach.profile.user)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=coach.profile.user)
        if user_form.is_valid():
            user_form.save()
            return redirect_user(request.user)
    return render(request, 'edit_profile.html', {'form': user_form})


@login_required
@user_passes_test(is_manager)
def delete_player_profile(request, username):
    player = Player.objects.get(profile__user__username=username)
    # delete user as well
    player.profile.user.delete()
    player.delete()
    return redirect('manager_after_login')


@login_required
@user_passes_test(is_manager)
def delete_coach_profile(request, username):
    coach = Coach.objects.get(profile__user__username=username)
    coach.profile.user.delete()
    coach.delete()
    return redirect('manager_after_login')
