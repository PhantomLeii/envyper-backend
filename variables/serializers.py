from rest_framework import serializers
from .models import Variable


class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable
        fields = "__all__"
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def validate(self, attrs):
        if self.partial:
            return attrs
        if not attrs.get("key"):
            raise serializers.ValidationError("Key field is required")
        if not attrs.get("value"):
            raise serializers.ValidationError("Value field is required")
        return attrs
