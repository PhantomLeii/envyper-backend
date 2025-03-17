from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


User = get_user_model()


@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({serializer.errors}, status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response({"data": serializer.data}, status.HTTP_201_CREATED)


@api_view(["GET"])
def get_user(request):
    try:
        user = User.objects.get(email=request.user)
        serializer = UserSerializer(user)
        return Response({"data": serializer.data}, status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def update_user(request):
    try:
        user = User.objects.get(email=request.user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"data": serializer.data}, status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_user(request):
    try:
        user = User.objects.get(email=request.user)
        user.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status.HTTP_404_NOT_FOUND)
