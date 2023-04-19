from django.shortcuts import render, redirect
from .models import Player, Coach, Manager, Profile
from .forms import PlayerForm, CoachForm, UserForm, ProfileForm
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash


def whiteboard(request):
    return render(request, 'whiteboard.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('player_list')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'login.html', {})


def create_profile(user_form, profile_form):
    username = user_form.cleaned_data['username']
    password = user_form.cleaned_data['password1']
    first_name = user_form.cleaned_data['first_name']
    last_name = user_form.cleaned_data['last_name']
    role = profile_form.cleaned_data['role']
    phone_number = profile_form.cleaned_data['phone_number']
    date_of_birth = profile_form.cleaned_data['date_of_birth']
    user = User.objects.create_user(
        username, password=password, first_name=first_name, last_name=last_name)
    profile = Profile.objects.create(
        user=user, phone_number=phone_number, date_of_birth=date_of_birth)
    if role == 'P':

        group = Group.objects.get_or_create(name='Players')[0]
        user.groups.add(group)

        profile = Player(profile=profile)
        profile.save()
        print("saved player")
    elif role == 'C':
        group = Group.objects.get_or_create(name='Coaches')[0]
        user.groups.add(group)

        profile = Coach(profile=profile)
        profile.save()
    elif role == 'M':
        group = Group.objects.get_or_create(name='Managers')[0]
        user.groups.add(group)

        profile = Manager(profile=profile)
        profile.save()
    return user


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

            return redirect('player_list')

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def player_list(request):
    players = Player.objects.all()
    return render(request, 'player_list.html', {'players': players})


@login_required
def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'player_form.html', {'form': form})


@login_required
def player_update(request, pk):
    player = Player.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'player_form.html', {'form': form})


@login_required
def player_delete(request, pk):
    player = Player.objects.get(pk=pk)
    player.delete()
    return redirect('player_list')


def coach_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coach_list.html', {'coaches': coaches})


def coach_create(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coach_list')
    else:
        form = CoachForm()
    return render(request, 'coach_form.html', {'form': form})


def coach_update(request, pk):
    coach = Coach.objects.get(pk=pk)
    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coach_list')
    else:
        form = CoachForm(instance=coach)
    return render(request, 'coach_form.html', {'form': form})


def coach_delete(request, pk):
    coach = Coach.objects.get(pk=pk)
    coach.delete()
    return redirect('coach_list')