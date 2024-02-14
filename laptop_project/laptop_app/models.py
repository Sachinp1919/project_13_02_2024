from django.db import models


class Laptop(models.Model):
    laptop_name = models.CharField(max_length=20)
    laptop_model = models.CharField(max_length=20)
    storage = models.IntegerField()
    ram = models.IntegerField()
    price = models.FloatField()
