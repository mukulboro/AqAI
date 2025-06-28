from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("A user must have an email")
        if not password:
            raise ValueError("A user must have a password")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_public", False)
        kwargs.setdefault("is_municipal", False)
        kwargs.setdefault("is_superuser", False)
        return self.create_user(email, password, **kwargs)
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    is_municipal = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_google = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    
    objects = CustomUserManager()
    
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    def __str__(self):
        return self.email
    