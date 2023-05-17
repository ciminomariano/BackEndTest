from django.db import models


class Dividend(models.Model):
    symbol = models.CharField(max_length=20)
    date = models.DateField()
    amount = models.FloatField()

