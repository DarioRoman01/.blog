"""Post models."""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User

class Post(models.Model):
    """Post model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile =  models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='posts/pictures')

    resume = models.CharField(max_length=255)

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return user and title."""
        return '{} by @ {}'.format(self.title, self.user.username)

class Comment(models.Model):
    """Comments model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    content = models.CharField(max_length=255)

    def __str__(self):
        return 'comment by @{}'.format(self.user.username)
    
    