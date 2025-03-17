from django.urls import path
from .views import get_user, create_user, delete_user, update_user

urlpatterns = [
    path("", get_user, name="list-user"),
    path("create/", create_user, name="create-user"),
    path("update/", update_user, name="update-user"),
    path("delete/", delete_user, name="delete-user"),
]
