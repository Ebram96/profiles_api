from django.urls import path
from profiles_api import views

urlpatterns = [
    path("hello-world/", views.HelloAPIView.as_view(), name="hello_world_api"),
]
