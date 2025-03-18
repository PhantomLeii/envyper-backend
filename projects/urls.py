from django.urls import path
from .views import ProjectsAPIView, ProjectDetailAPIView


urlpatterns = [
    path("", ProjectsAPIView.as_view(), name="projects"),
    path("<int:pk>/", ProjectDetailAPIView.as_view(), name="projects-detail"),
]
