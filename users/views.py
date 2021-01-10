"""Users views."""

# Django 
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Views and auth_views
from django.contrib.auth import views as auth_views
from django.views.generic import (
    UpdateView,
    FormView,
    DetailView,
    ListView
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
        """Add user's posts to context and check if the requesting user(user_from)
         already follows the user(user)"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        user_from = self.request.user

        follows = False
        if user_from.follow.filter(id=user.id).exists():
            follows = True

        context['follows'] = follows
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

def FollowView(request, username):
    """Follow view."""

    user = get_object_or_404(User, username=request.POST.get('user_username'))
    user_from = request.user
    follows = False

    if user_from.follow.filter(id=user.id).exists():
        user_from.follow.remove(user)
        follows = False
        user.profile.followers -= 1
        user.profile.save()

    else:
        user_from.follow.add(user)
        follows = True
        user.profile.followers += 1
        user.profile.save()

    return HttpResponseRedirect(reverse('users:detail', kwargs={'username': request.POST.get('user_username')}))


class UsersToFollowView(LoginRequiredMixin, ListView):
    """Users to follow view, return all the users that the requesting
    user is not following."""

    template_name = 'users/new_folow.html'
    model = User
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'users'

    def get_queryset(self):
        user = self.request.user

        id_list = []
        follow_list = list(user.follow.all())

        for i in follow_list:
            id_list.append(i.id)
        id_list.append(user.id)
        
        return User.objects.exclude(id__in=id_list)
    