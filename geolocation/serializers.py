from rest_framework import serializers
from .models import Location

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

class NewLocationSerializer(serializers.Serializer):
    #url = serializers.URLField(required=False, default=None)
    ip = serializers.IPAddressField(required=False, default=None)

    # def validate(self, data):
    #     if data['url'] is not None and data['ip'] is not None:
    #         raise serializers.ValidationError("You must provide either a full url or an ip address.")
    #     elif data['url'] is None and data['ip'] is None:
    #         raise serializers.ValidationError("You must provide either a full url or an ip address.")
    #     else:
    #         return data