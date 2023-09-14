from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm, UserUpdateForm
from accounts.views import *

app_name="accounts"
urlpatterns=[
    path("login/", LoginView.as_view(
        redirect_authenticated_user=True,
        template_name="login.html"
    ),name="login" ), 
    path("signup/", CreateView.as_view(
        form_class=CustomUserCreationForm,
        success_url="login",
        template_name="signup.html"
    ),name="signup" ), 
    path("user_details/", UserDetails.as_view(), name="signup" ), 
    
]
