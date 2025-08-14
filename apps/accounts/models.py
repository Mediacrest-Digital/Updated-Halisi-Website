import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, fullname, phone, password=None):
        if not email:
            raise ValueError("Email is required")
        
        user = self.model(
            email=self.normalize_email(email).lower(),
            fullname=fullname,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, fullname, phone, password=None):
        if not email:
            raise ValueError("Email is required")

        user = self.create_user(
            email=email,
            fullname=fullname,
            phone=phone,
            password=password,
        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'fullname', 'phone'
    ]

    def __str__(self):
        return f"{self.email}"

