from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views
from geolocation import views
urlpatterns = [
    path('', views.api_root),
    path('locations/', views.LocationListView.as_view(), name='locations_list'),
    path('locations/<int:pk>/', views.LocationDetailsView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)