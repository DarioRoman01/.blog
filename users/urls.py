"""users urls."""

# Django
from django.urls import path
from users import views

urlpatterns = [
     path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='signup/',
        view=views.SingUpView.as_view(),
        name='signup'
    ),
    path(
        route='<str:username>/profile',
        view=views.ProfileDetailView.as_view(),
        name='detail'
    ),
    path(
        route='<str:username>/profile/follow',
        view=views.FollowView,
        name='follow'
    ),
    path(
        route='explore/people',
        view=views.UsersToFollowView.as_view(),
        name='explore'
    ),
    path(
        route='me/update',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),
    path(
        route='logout',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
]
