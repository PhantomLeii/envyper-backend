from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProjectSerializer
from .models import Projects


class ProjectsAPIView(APIView):
    def get(self, request):
        projects = Projects.objects.filter(creator=request.user)
        serializer = ProjectSerializer(projects)
        return Response({"data": serializer.data}, status.HTTP_200_OK)

    def post(self, request):
        pass


class ProjectDetailAPIView(APIView):
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
