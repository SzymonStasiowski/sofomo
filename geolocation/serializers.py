from rest_framework import serializers
from .models import Location
from .geolocation import get_geolocation

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['ip',
                  'type',
                  'continent_code',
                  'continent_name',
                  'country_code',
                  'country_name',
                  'region_code',
                  'region_name',
                  'city',
                  'zip',
                  'latitude',
                  'longitude']

class InputSerializer(serializers.Serializer):
    link = serializers.RegexField(regex='(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+',
                                  required=False,
                                  default=None)
    ip = serializers.IPAddressField(required=False, default=None)
