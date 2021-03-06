from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()

router.register("hello-viewset", views.HelloViewSet, base_name="hello_viewset")
router.register("profile", views.UserProfileViewSet)
router.register("login", views.LoginViewSet, base_name="login_viewset")
router.register("feed", views.FeedItemViewSet)

urlpatterns = [
    path("hello-world/", views.HelloAPIView.as_view(), name="hello_world_api"),
    path("", include(router.urls))
]
