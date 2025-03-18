from django.urls import path
from .views import ProjectsAPIView


urlpatterns = [path("", ProjectsAPIView.as_view(), name="projects")]
