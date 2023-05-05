from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
#import phone_field


# make email unique
User._meta.get_field('email')._unique = True


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
    pending_payment = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    # team = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"


class Coach(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"


class Manager(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"


class Notification(models.Model):
    owner = models.ForeignKey(
        Profile, related_name='notifications_owned', on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.created_at.strftime(' %Y-%m-%d %H: %M: %S')} - {self.profile.user.username}: {self.message}"


class Payment(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.player.profile.user.username} - {self.amount}"


class Announcement(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class CanvasImage(models.Model):
    title = models.CharField(max_length=100, default='Untitled')
    image_data = models.TextField()
    # add default time stamp
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
