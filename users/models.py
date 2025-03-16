from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        """Create a user with the provided email, password & extra fields"""
        if not email:
            raise ValueError("Email field is required")

        if not password:
            raise ValueError("Password field is required")

        if not extra_fields.get("first_name"):
            raise ValueError("First Name field is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        Create a superuser with the provided email, password & extra fields.
        Also sets is_staff & is_superuser fields to True by default
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        superuser = self.create_user(email, password, **extra_fields)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.CharField(_("Email"), max_length=255, unique=True)
    first_name = models.CharField(_("First Name"), max_length=150, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=150, blank=True)

    is_staff = models.BooleanField(_("Staff Member"), default=False)
    is_superuser = models.BooleanField(_("Superuser"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name",)

    objects = UserManager()

    def __str__(self):
        return self.email
