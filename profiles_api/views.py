from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloAPIView(APIView):
    """A hello world API view"""
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
