"""Post urls."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostFeedView.as_view(),
        name='feed'
    ),
    path(
        route='posts/create',
        view=views.CreatePostView.as_view(),
        name='create'
    ),
    path(
        route='posts/<int:id>',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
        route='posts/<int:id>/delete',
        view=views.DeletePostView.as_view(),
        name='delete'
    ),
    path(
        route='posts/<int:id>/update',
        view=views.UpdatePostView.as_view(),
        name='update'
    ),
    path(
        route='posts/<int:id>/comments',
        view=views.AddCommentView.as_view(),
        name='comment'
    )
]
