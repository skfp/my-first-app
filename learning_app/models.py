from django.db import models


class Card(models.Model):
    front = models.CharField(max_length=100)
    back = models.CharField(max_length=100)


