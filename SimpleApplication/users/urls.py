from django.urls import path
from . import views

urlpatterns = [
    path("", views.users_detail, name="users_detail"),
    path("<int:id>", views.get_user, name="get_user"),
]
