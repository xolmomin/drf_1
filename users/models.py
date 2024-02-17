from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CASCADE, CharField
from mptt.models import MPTTModel, TreeForeignKey


class User(AbstractUser):
    image = ImageField(null=True, blank=True)


class Category(MPTTModel):
    name = CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Ketagoriya'
        verbose_name_plural = 'Ketagoriyalar'

    def __str__(self):
        return self.name
