from django.contrib.auth.models import User
from django.db import models


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
    # team = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"


class Manager(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # team = models.CharField(max_length=50)

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

# class Schedule(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     event_type = models.CharField(max_length=50)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     location = models.CharField(max_length=255)

#     def __str__(self):
#         return f'{self.event_type} - {self.start_time}'

# class Game(models.Model):
#     home_team = models.ForeignKey(Team, related_name='home_team', on_delete=models.CASCADE)
#     away_team = models.ForeignKey(Team, related_name='away_team', on_delete=models.CASCADE)
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50)

#     def __str__(self):
#         return f'{self.home_team} vs {self.away_team}'

# class Practice(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50)

#     def __str__(self):
#         return f'{self.team} - {self.status}'

# class Statistic(models.Model):
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     points = models.IntegerField()
#     rebounds = models.IntegerField()
#     assists = models.IntegerField()
#     steals = models.IntegerField()
#     blocks = models.IntegerField()

#     def __str__(self):
#         return f'{self.user} - {self.game}'


# class Playbook(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     item = models.ForeignKey('WhiteboardItem', on_delete=models.CASCADE, related_name='playbook_items', null=True, blank=True)
#     def __str__(self):
#         return str(self.item)

# class WhiteboardItem(models.Model):
#     playbook = models.ForeignKey(Playbook, on_delete=models.CASCADE, related_name='whiteboard_items')
#     play_name = models.CharField(max_length=255)
#     play_description = models.TextField()
#     play_diagram= models.FileField(upload_to='playbook/', blank=True, null=True)

#     def __str__(self):
#         return self.play_name

# class Payment(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     due_date = models.DateField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_status = models.CharField(max_length=50)

#     def __str__(self):
#         return f'{self.user} - {self.amount}'

# class AuditTrail(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     action = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)

# def __str__(self):
#     return f'{self.user} - {self.action} - {self.timestamp}'
