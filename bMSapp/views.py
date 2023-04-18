from django.shortcuts import render, redirect
from .models import Player, Coach
from .forms import PlayerForm, CoachForm, LoginForm
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout

def whiteboard(request):
    return render(request, 'whiteboard.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('player_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Updated to use auth_login
            return redirect('player_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

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
