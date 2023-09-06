from . import views
from django.urls import path

urlpatterns = [
    path("", views.Home, name="Home"),
    path("register/", views.Register, name="Register"),
    path("login/", views.Login, name="Login"),
    path("dashboard/", views.Dashboard, name="Dashboard"),
    path("logout/", views.LogoutUser, name="LogoutUser"),
    path("create_record/", views.CreateRecords, name="CreateRecord"),
    path("update_record/<int:pk>", views.UpdateRecords, name="UpdateRecords"),
    path("singular_record/<int:pk>", views.SingularRecords, name="SingularRecords"),
    path("delete_record/<int:pk>", views.DeleteRecords, name="DeleteRecords"),
]
