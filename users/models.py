from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CASCADE, CharField, Model, IntegerField, TextField, ForeignKey, BooleanField, \
    TextChoices
from mptt.models import MPTTModel, TreeForeignKey


class User(AbstractUser):
    image = ImageField(null=True, blank=True)
    is_vip = BooleanField(default=False)


class Category(MPTTModel):
    name = CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Ketagoriya'
        verbose_name_plural = 'Ketagoriyalar'

    def __str__(self):
        return self.name


class Product(Model):
    title = CharField(max_length=50, unique=True)
    price = IntegerField()
    description = TextField(null=True, blank=True)
    is_premium = BooleanField(default=False)
    is_new = BooleanField(default=0)
    category = ForeignKey('users.Category', CASCADE)

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        return self.title

# product list, delete, detail
# category list
# http://localhost:8000/api/v1/users/?username__startswith=use&username__endswith=1
# username=15
# API
