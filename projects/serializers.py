from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        extra_kwargs = {
            "updated_at": {"read_only": True},
            "created_at": {"read_only": True},
        }

    def validate(self, attrs):
        if self.partial:
            return attrs

        if not attrs.get("name"):
            raise serializers.ValidationError("Name field is required")
        return attrs
