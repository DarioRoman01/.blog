"""Users forms."""

# Django
from django import forms

# Models 
from django.contrib.auth.models import User
from users.models import Profile

class SignUpForm(forms.Form):
    """Sign up form"""
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=3)
    last_name = forms.CharField(min_length=3)

    email = forms.CharField(max_length=70, widget=forms.EmailInput())

    def clean_username(self):
        """User name must be unique."""

        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Sorry that username is already in use')
        return username

    def clean(self):
        """Verify that password mathcs."""
        data = super().clean()

        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise forms.ValidationError('Passwords does not match')
        return data

    def save(self):
        """Create user and profile."""

        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class UpdateProfileForm(forms.ModelForm):
    """Update profile form."""

    class Meta:
        """Meta class."""
        model=Profile
        fields=(
            'user',
            'biography',
            'picture'
        )