from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


User = get_user_model()


class CreateUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"data": serializer.data}, status.HTTP_201_CREATED)


class UserAPIView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(email=request.user)
            serializer = UserSerializer(user)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"message": "User does not exist"}, status.HTTP_404_NOT_FOUND
            )
