from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')

    def __str__(self) -> str:
        return self.email
