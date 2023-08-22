from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_new_user, name="register_user"),
    path("create_user", views.create_user, name="create_user"),
]
