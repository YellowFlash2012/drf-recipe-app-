from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        user=self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD="email"

class Recipe(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cooking_time = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.name