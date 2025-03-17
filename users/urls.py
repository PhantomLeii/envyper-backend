from django.urls import path
from .views import UserAPIView, CreateUserAPIView

urlpatterns = [
    path("", UserAPIView.as_view(), name="list-user"),
    path("create/", CreateUserAPIView.as_view(), name="create-user"),
]
