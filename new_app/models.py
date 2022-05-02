from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from .managers import UserManager

class NewUser(AbstractBaseUser):

    email = models.EmailField( unique=True)
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    date_joined = models.DateTimeField( default=timezone.now)
    objects = UserManager()

    EMAIL_FIELD = "email"

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


    
   