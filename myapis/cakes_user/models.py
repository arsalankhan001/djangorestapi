from django.db import models
from cakesdata.models import Cakes


class UserDetails(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    cart = models.ManyToManyField(Cakes)

    def __str__(self):
        return self.name

