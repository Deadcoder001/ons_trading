from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Price(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date = models.DateField()
    close = models.FloatField()

class PortfolioWeight(models.Model):
    date = models.DateField(auto_now_add=True)
    weights = models.JSONField(default=dict)  # for a dictionary of weights
    # or
    # weight = models.FloatField(default=0)   # for a single float value
