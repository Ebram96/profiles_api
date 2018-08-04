from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name for testing API view"""
    first_name = serializers.CharField(max_length=256)
    last_name = serializers.CharField(max_length=256)
