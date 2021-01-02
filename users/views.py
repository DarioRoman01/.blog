"""Users views."""

# Django 
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

# Views and auth_views
from django.contrib.auth import views as auth_views
from django.views.generic import (
    UpdateView,
    FormView,
    DetailView
)

# Forms
from users.forms import SignUpForm, UpdateProfileForm

# Models
from posts.models import Post
from users.models import Profile
from django.contrib.auth.models import User


class SingUpView(FormView):
    """Sing up view."""
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        #save form data
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'users/logged_out.html'


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view. the users are redirect to this view
    if they do his first login."""

    template_name = 'users/update.html'
    model = Profile
    fields = ['picture', 'biography']
    context_object_name = 'profile'
    queryset = Profile.objects.all()

    def get_success_url(self):
        username = self.request.user.username
        return reverse('users:detail', kwargs={'username': username})

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user 
        return context
    

class ProfileDetailView(LoginRequiredMixin, DetailView):
    """Profile detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


    


    
