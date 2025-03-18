from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProjectSerializer
from .models import Projects


class ProjectsAPIView(APIView):
    def get(self, request):
        projects = Projects.objects.filter(creator=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response({"data": serializer.data}, status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(
            data={**request.data, "creator": request.user.id}
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"data": serializer.data}, status.HTTP_201_CREATED)


class ProjectRetrievalMixin:
    def get_queryset(self):
        """
        Get all projects owned my the authenticated user
        """
        return Projects.objects.filter(creator=self.request.user)

    def get_project(self, pk):
        """
        Get the project with the given PK value from
        the queryset
        """
        queryset = self.get_queryset()
        try:
            project = queryset.get(pk=pk)
            return project
        except Projects.DoesNotExist:
            return None


# TODO: TEST ALL VIEWS
class ProjectDetailAPIView(APIView, ProjectRetrievalMixin):
    def get(self, request, pk):
        project = self.get_project(pk)
        if project is None:
            return Response(
                {"message": "User does not own a project with the given ID"},
                status.HTTP_404_NOT_FOUND,
            )

        serializer = ProjectSerializer(project)
        return Response({"data": serializer.data}, status.HTTP_200_OK)

    def put(self, request, pk):
        project = self.get_project(pk)
        if project is None:
            return Response(
                {"message": "User does not own a project with the given ID"},
                status.HTTP_404_NOT_FOUND,
            )

        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                {"message": "Provided data is invalid"}, status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response({"data": serializer.data}, status.HTTP_200_OK)

    def delete(self, request, pk):
        project = self.get_project(pk)
        if project is None:
            return Response(
                {"message": "User does not own a project with the given ID"},
                status.HTTP_404_NOT_FOUND,
            )

        project.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)
