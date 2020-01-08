from django.shortcuts import render
from .models import Location
from .serializers import LocationSerializer, NewLocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .geolocation import get_geolocation

# Create your views here.
class LocationList(APIView):

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        input_serializer = NewLocationSerializer(data=request.data)
        if input_serializer.is_valid():
            serializer = LocationSerializer(data=get_geolocation(input_serializer.validated_data['ip']))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)