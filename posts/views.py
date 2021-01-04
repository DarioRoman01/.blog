"""Posts views."""

# Django 
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

# Views and auth_views
from django.contrib.auth import views as auth_views
from django.views.generic import (
    UpdateView,
    FormView,
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)

# Forms
from posts.forms import CreatePostForm

# Models
from posts.models import Post, Comment
from users.models import Profile
from django.contrib.auth.models import User


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create post view."""
    template_name = 'posts/create.html'
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to the context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile 
        return context

    def post(self, request, *args, **kwargs):
        """added 1 to blog_posted counter of the user"""
        username = self.request.user.username
        profile = Profile.objects.get(user__username=username)
        profile.blog_posted += 1
        profile.save()
        return super().post(request, *args, **kwargs)

class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Post detail view. return a especific post."""

    template_name = 'posts/detail.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_context_data(self, **kwargs):
        """add comments to the context."""
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("id")
        post = Post.objects.get(pk=id_)
        context["comments"] = post.comment_set.all()
        return context
    

class DeletePostView(LoginRequiredMixin, DeleteView):
    """Delete post view."""
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:feed')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def post(self, request, *args, **kwargs):
        """subtract 1 from the blog_posted counter of the user."""  
        username = self.request.user.username
        profile = Profile.objects.get(user__username=username)
        profile.blog_posted -= 1
        profile.save()
        return self.delete(request, *args, **kwargs)
        

class UpdatePostView(LoginRequiredMixin, UpdateView):
    """Update post view."""
    template_name = 'posts/create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts:feed')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_context_data(self, **kwargs):
        """Add user and profile to the context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile 
        return context

class AddCommentView(LoginRequiredMixin, CreateView):
    """Add comment view."""
    template_name = 'comments/new.html'
    model = Comment
    fields = ['user', 'profile', 'post', 'content']

    def get_object(self):
        """Get post id."""
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_context_data(self, **kwargs):
        """add users, profile and post to the context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        id_ = self.kwargs.get("id")
        context['post'] = Post.objects.get(pk=id_)   
        return context

    def get_success_url(self):
        id_ = self.kwargs.get("id")
        return reverse('posts:detail', kwargs={'id': id_})
    
