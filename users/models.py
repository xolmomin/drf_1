from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField


class User(AbstractUser):
    image = ImageField(null=True, blank=True)
