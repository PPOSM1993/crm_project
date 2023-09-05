from . import views
from django.urls import path

urlpatterns = [
    path("", views.Home, name="Home"),
    path("register/", views.Register, name="Register"),
    path("login/", views.Login, name="Login"),
    path("dashboard/", views.Dashboard, name="Dashboard"),
    path("logout/", views.LogoutUser, name="LogoutUser"),

]
