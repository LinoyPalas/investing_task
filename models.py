from django.db import models


class AdUnit(models.Model):
    """
    AdUnit model to store information about ad containers
    """
    country = models.CharField(max_length=3)
    language = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.country}-{self.language}-{self.device}-{self.os}-{self.browser}"
