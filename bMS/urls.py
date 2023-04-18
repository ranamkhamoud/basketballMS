"""bMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from bMSapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('whiteboard/', views.whiteboard, name='whiteboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('players/', views.player_list, name='player_list'),
    path('player/create/', views.player_create, name='player_create'),
    path('player/update/<int:pk>/', views.player_update, name='player_update'),
    path('player/delete/<int:pk>/', views.player_delete, name='player_delete'),
    path('coaches/', views.coach_list, name='coach_list'),
    path('coach/create/', views.coach_create, name='coach_create'),
    path('coach/update/<int:pk>/', views.coach_update, name='coach_update'),
    path('coach/delete/<int:pk>/', views.coach_delete, name='coach_delete'),
    path('login/', views.login),

]


