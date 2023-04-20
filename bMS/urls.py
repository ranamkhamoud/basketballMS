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
    path('', views.user_login, name='login'),
    path('admin/', admin.site.urls),
    path('whiteboard/', views.whiteboard, name='whiteboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('player/', views.player_after_login, name='player_after_login'),
    path('coach/', views.coach_after_login, name='coach_after_login'),
    path('manager/', views.manager_after_login, name='manager_after_login'),
    path('edit_player_profile/<str:username>/',
         views.edit_player_profile, name='edit_player_profile'),
    path('edit_coach_profile/<str:username>/',
         views.edit_coach_profile, name='edit_coach_profile'),
    path('delete_player_profile/<str:username>/',
         views.delete_player_profile, name='delete_player_profile'),
    path('delete_coach_profile/<str:username>/',
         views.delete_coach_profile, name='delete_coach_profile'),



]


