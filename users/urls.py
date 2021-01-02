"""users urls."""

# Django
from django.urls import path
from users.views import (
    LoginView,
    SingUpView,
    UpdateProfileView,
    ProfileDetailView,
    LogoutView
)

urlpatterns = [
     path(
        route='login/',
        view=LoginView.as_view(),
        name='login'
    ),
    path(
        route='signup/',
        view=SingUpView.as_view(),
        name='signup'
    ),
    path(
        route='<str:username>/profile',
        view=ProfileDetailView.as_view(),
        name='detail'
    ),
    path(
        route='me/update',
        view=UpdateProfileView.as_view(),
        name='update'
    ),
    path(
        route='logout',
        view=LogoutView.as_view(),
        name='logout'
    ),
]
