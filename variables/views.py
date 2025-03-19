from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Variable
from projects.models import Projects
from .serializers import VariableSerializer


class VariableRetrivalMixin:
    @staticmethod
    def get_project(user_id, project_id):
        """
        Get a project owned by the authenticated user
        with the provided project ID
        """
        try:
            project = Projects.objects.get(creator=user_id, pk=project_id)
            return project
        except Projects.DoesNotExist:
            return None

    def get_queryset(self, user_id, project_id):
        """
        Get all variables owned by the project with the provided
        project ID
        """
        project = self.get_project(user_id, project_id)
        if project is None:
            raise Projects.DoesNotExist

        variables = Variable.objects.filter(project=project.id)
        return variables

    def get_variable(self, user_id, project_id, pk):
        """
        Get the variable owned by the project with the provided
        project ID by its ID
        """
        project = self.get_project(user_id, project_id)
        if project is None:
            raise Projects.DoesNotExist

        return Variable.objects.get(pk=pk, project=project_id)


class VariablesAPIView(APIView, VariableRetrivalMixin):
    def get(self, request, project_id):
        try:
            variables = self.get_queryset(request.user.id, project_id)
            serializer = VariableSerializer(variables, many=True)
            return Response({"data": serializer.data}, status.HTTP_200_OK)
        except Projects.DoesNotExist:
            return Response(
                {
                    "message": "User is not associated with the project of the provided ID"
                },
                status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, project_id):
        try:
            project = self.get_project(request.user.id, project_id)

            serializer = VariableSerializer(
                data={**request.data, "project": project.id}
            )
            if not serializer.is_valid():
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({"data": serializer.data}, status.HTTP_201_CREATED)
        except Projects.DoesNotExist:
            return Response(
                {
                    "message": "User is not associeated with a project of the provided ID"
                },
                status.HTTP_404_NOT_FOUND,
            )


class VariableDetailAPIView(APIView, VariableRetrivalMixin):
    def get(self, request, project_id, pk):
        try:
            variable = self.get_variable(request.user.id, project_id, pk)
            if variable is None:
                return Response(
                    {
                        "message": "Project is not associated with a variable of the provided ID"
                    },
                    status.HTTP_404_NOT_FOUND,
                )

            seriaizer = VariableSerializer(variable)
            return Response({"data": seriaizer.data}, status.HTTP_200_OK)
        except Variable.DoesNotExist:
            return Response(
                {"message": "Variable with the provided ID does not exist"},
                status.HTTP_404_NOT_FOUND,
            )
        except Projects.DoesNotExist:
            return Response(
                {"message": "User is not associated with a project of the provided ID"},
                status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, project_id, pk):
        try:
            variable = self.get_variable(request.user.id, project_id, pk)
            serializer = VariableSerializer(
                variable, data={**request.data, "project": project_id}, partial=True
            )
            if not serializer.is_valid():
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({"data": serializer.data}, status.HTTP_200_OK)
        except Variable.DoesNotExist:
            return Response(
                {"message": "Variable with the provided ID does not exist"},
                status.HTTP_404_NOT_FOUND,
            )
        except Projects.DoesNotExist:
            return Response(
                {"message": "User is not associated with a project of the provided ID"},
                status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, project_id, pk):
        try:
            variable = self.get_variable(request.user.id, project_id, pk)
            variable.delete()
            return Response({}, status.HTTP_204_NO_CONTENT)
        except Variable.DoesNotExist:
            return Response(
                {"message": "Variable with the provided ID does not exist"},
                status.HTTP_404_NOT_FOUND,
            )
        except Projects.DoesNotExist:
            return Response(
                {"message": "User is not associated with a project of the provided ID"},
                status.HTTP_404_NOT_FOUND,
            )
