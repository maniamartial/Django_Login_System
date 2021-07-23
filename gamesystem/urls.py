from django.urls import path
from .import views

urlpatterns = [
    path("login", views.loginsystem, name="login"),
    path("register", views.registersystem, name="register"),
    path("", views.home, name="home")
]
