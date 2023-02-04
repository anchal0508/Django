from django.db import models

class members(models.Model):
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    father = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

