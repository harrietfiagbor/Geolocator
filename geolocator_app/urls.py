from django.urls import path
from . import views

app_name = "geolocator"

urlpatterns = [
    path('', views.coordinates_form, name="coordinates-form"),
    path('map', views.maps, name="map")
]
