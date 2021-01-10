"""Users models."""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile model holds the public information of the user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    biography = models.TextField(max_length=500, blank=True)

    picture = models.ImageField(
        'profile image',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    
    followers = models.PositiveIntegerField(default=0)
    blog_posted = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
    

User.add_to_class('follow', models.ManyToManyField('self', related_name='following', symmetrical=False))