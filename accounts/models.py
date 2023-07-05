from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ic = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    subscribe = models.BooleanField(default=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    @property
    def is_guard(self):
        return self.is_active and (
            self.is_superuser
            or self.is_staff
            and self.groups.filter(name="guard").exists()
        )

    @property
    def is_resident(self):
        return self.is_active and (
            self.is_superuser
            or self.is_staff
            and self.groups.filter(name="resident").exists()
        )
