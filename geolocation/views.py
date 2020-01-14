from django.shortcuts import render
from .models import Location
from .serializers import LocationSerializer, InputSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as jwt_views
from django.http import Http404
from .geolocation import get_geolocation

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'locations': reverse('locations_list', request=request, format=format),
        'token': reverse('token_obtain_pair', request=request, format=format),
        'refresh': reverse('token_refresh', request=request, format=format),
    })

class LocationListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)


# paskudny kod
    def post(self, request):
        input_serializer = InputSerializer(data=request.data)
        if input_serializer.is_valid():
            if input_serializer.validated_data['link']:
                data = get_geolocation(input_serializer.validated_data['link'])
                model_serializer = LocationSerializer(data=data)
                if model_serializer.is_valid():
                    model_serializer.save()
                    return Response(model_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(model_serializer.errors, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            elif input_serializer.validated_data['ip']:
                data = get_geolocation(input_serializer.validated_data['ip'])
                model_serializer = LocationSerializer(data=data)
                if model_serializer.is_valid():
                    model_serializer.save()
                    return Response(model_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(model_serializer.errors, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetailsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def delete(self, request, pk):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)