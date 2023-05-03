from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username


class Player(models.Model):

    position_choices = [
        ('PG', 'Point Guard'),
        ('SG', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center'),

    ]

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, choices=position_choices)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"


class Coach(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"


class Manager(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # team = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"


class CanvasImage(models.Model):
    title = models.CharField(max_length=100, default='Untitled')
    image_data = models.TextField()
    # add default time stamp
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
