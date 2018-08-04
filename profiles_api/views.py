from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers, models
# Create your views here.


class HelloAPIView(APIView):
    """A hello world API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns APIView features list"""
        api_dict = {
            "message": "Hello World!",
            "API_view": [
                "Uses HTTP methods as functions (get, post, patch, put, delete).",
                "Similar to Django view",
                "Mapped manually ot URLs",
            ]
        }

        return Response(api_dict)

    def post(self, request):
        """Returns a hello message with a name"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            first_name = serializer.data.get("first_name")
            last_name = serializer.data.get("last_name")
            message = "Hello " + first_name + " " + last_name

            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Updates an object"""
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """Partially updates an object"""
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({"method": "delete"})
