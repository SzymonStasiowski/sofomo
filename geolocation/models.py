from django.db import models

# Create your models here.
class Location(models.Model):
    ip = models.CharField(max_length=15)
    type = models.CharField(max_length=4)
    continent_code = models.CharField(max_length=5)
    continent_name = models.CharField(max_length=30)
    country_code = models.CharField(max_length=5)
    country_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=5)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    latitude = models.FloatField()
    longitude = models.FloatField()
