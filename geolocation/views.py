from django.shortcuts import render
from .models import Location
from .serializers import LocationSerializer, InputSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .geolocation import get_geolocation

# Create your views here.

class LocationView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        input_serializer = InputSerializer(data=request.data)
        if input_serializer.is_valid():
            data = get_geolocation(next(iter(input_serializer.validated_data)))
            model_serializer = LocationSerializer(data=data)
            if model_serializer.is_valid():
                model_serializer.save()
                return Response(model_serializer.data, status=status.HTTP_201_CREATED)
            return Response(model_serializer.errors, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)