from django.urls import path
from .views import VariablesAPIView, VariableDetailAPIView


urlpatterns = [
    path("<int:project_id>/", VariablesAPIView.as_view(), name="variables"),
    path(
        "<int:project_id>/<int:pk>/",
        VariableDetailAPIView.as_view(),
        name="variable-detail",
    ),
]
