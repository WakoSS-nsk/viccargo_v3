from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50,
                                  blank=False,
                                  null=False)
    last_name = models.CharField(max_length=50,
                                 blank=False,
                                 null=False)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=150,
                                    blank=True,
                                    null=True)
    phone_number = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.username}: AbstractUser instance.'
