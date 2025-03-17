from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "created_at": {"read_only": True},
        }

    def validate(self, attrs):
        """Validate that the Email, Password & First name fields are populated"""
        if not attrs.get("email"):
            raise serializers.ValidationError("Email field is required")

        if not attrs.get("first_name"):
            raise serializers.ValidationError("First name field is required")

        if not attrs.get("password"):
            raise serializers.ValidationError("Password field is required")

        return attrs
