from django.db import models


class AdUnit(models.Model):
    """
    AdUnit model to store information about ad containers
    """
    country = models.CharField(max_length=3)  # ISO-3166 max char num is 3
    language = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.country}-{self.language}-{self.device}-{self.os}-{self.browser}"


class LineItem(models.Model):
    """
    LineItem model to store information about ad serving
    """
    max_impressions = models.PositiveIntegerField()
    rpm = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # Targeting that allows the advertiser to reach its intended audience or demographic
    # (implemented using the various ad units)
    ad_unit = models.ForeignKey(AdUnit, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.max_impressions}-{self.rpm}-{self.start_time}-{self.end_time}"


class Creative(models.Model):
    """
    Creative model to store information about ad content
    """

    CREATIVE_TYPE_CHOICES = [
        ('image', 'image'),
        ('html5', 'html5'),
        ('native', 'native')
    ]

    creative_type = models.CharField(max_length=100, choices=CREATIVE_TYPE_CHOICES)
    content = models.BinaryField()

    # how to represent the following in pixel - pixels, defined as width x height (300x100
    size = models.CharField(max_length=100)

    line_item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.creative_type}-{self.size}"
