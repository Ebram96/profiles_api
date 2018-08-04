from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from profiles_api import serializers, models, permissions
# Create your views here.


class HelloAPIView(APIView):
    """A hello world API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns APIView features list"""
        dat = [
            "Uses HTTP methods as functions (get, post, patch, put, delete).",
            "Similar to Django view",
            "Mapped manually ot URLs",
        ]

        return Response({"message": "Hello World!", "Data": dat})

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


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a hello world message"""
        dat = [
            "Uses actions: (list, create, retrieve, update, partial update).",
            "Maps to URLs using routers",
        ]

        return Response({"message": "Hello World! from viewset", "Data": dat})

    def create(self, request):
        """Creates a new hello message"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            first_name = serializer.data.get("first_name")
            last_name = serializer.data.get("last_name")
            message = "Hello " + first_name + " " + last_name

            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Gets an object by its ID"""

        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Updates an object"""

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Updates an object partially"""

        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Deletes an object"""

        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("email", "first_name")


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use ObtainAuthToken to validate and create a token"""

        return ObtainAuthToken().post(request)
