from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name for testing API view"""
    first_name = serializers.CharField(max_length=256)
    last_name = serializers.CharField(max_length=256)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for UserProfile model"""
    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "first_name", "last_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Creates and returns a new user"""

        user = models.UserProfile(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class FeedItemSerializer(serializers.ModelSerializer):
    """A serializer for FeedItem model."""
    class Meta:
        model = models.FeedItem
        fields = ("id", "user", "status", "created_on")
        extra_kwargs = {"user": {"read_only": True}}
