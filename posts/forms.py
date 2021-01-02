"""Posts forms."""

# Django
from django import forms

# Models 
from posts.models import Post

class CreatePostForm(forms.ModelForm):
    """Create post form."""

    class Meta:
        """Meta class."""
        model = Post
        fields = (
            'user',
            'profile',
            'title',
            'picture',
            'resume',
            'content'
        )



    