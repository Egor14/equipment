from django.db import models
from django.contrib.auth.models import User

class Dealer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    city = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return self.model