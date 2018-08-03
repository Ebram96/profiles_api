from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
# Create your models here.


class UserProfileManager(BaseUserManager):
    """The model manager for UserProfile model"""
    def create_user(self, email, first_name, last_name, password=None):
        """Creates a new UserProfile object"""
        if not email:
            raise ValueError("An email address must be provided!")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Creates and saves a super user"""
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user's profile"""
    email      = models.EmailField(max_length=256, unique=True, null=False)
    first_name = models.CharField(max_length=256)
    last_name  = models.CharField(max_length=256)
    is_active  = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)

    objects    = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    def get_full_name(self):
        """Returns user's full name"""
        return self.first_name + " " + self.last_name

