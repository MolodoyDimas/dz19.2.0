from django.db import models
from django.contrib.auth.models import AbstractUser
import random

code = ''.join([str(random.randint(0, 9)) for _ in range(12)])


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name='Страна', blank=True, null=True)

    is_active = models.BooleanField(default=False, verbose_name="Почта верифицирована")
    ver_code = models.CharField(max_length=15, default=code, verbose_name='Проверочный код')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
