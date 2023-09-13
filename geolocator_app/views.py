from django.shortcuts import render, redirect
from .models import *
from .forms import *

import folium

# Create your views here.

def coordinates_form(request):
    coordinates = Coordinate.objects.all()
    form = CoordinateForm()

    if request.method == 'POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("geolocator:map")
    context = {
        'coordinates': coordinates,
        'form': form
    }
    return render(request, "coord-form.html", context)


def maps(request):
    coordinates = list(Coordinate.objects.values_list('lat','lon'))[-1]
    print(coordinates)

    map = folium.Map(location=coordinates, tiles=None)

    fg = folium.FeatureGroup(name='coordinates')
    fg.add_child(folium.Marker(location=coordinates))
    map.add_child(fg)
    
    folium.raster_layers.TileLayer(tiles="OpenStreetMap").add_to(map)
    folium.raster_layers.TileLayer(tiles="Stamen Terrain", show=False).add_to(map)
    folium.raster_layers.TileLayer(tiles="Stamen Toner", show=False).add_to(map)
    folium.raster_layers.TileLayer(tiles="Stamen Watercolor", show=False).add_to(map)
    
    folium.LayerControl().add_to(map)

    map = map._repr_html_()
    context = {
        'map':map
    }
    return render(request, "map.html", context=context)
