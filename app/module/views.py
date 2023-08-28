from django.http import HttpResponse
from django.shortcuts import render
from .models import location
import folium

def show(request):
    # data = location.objects.all()
    data = location.objects.filter(type="รัฐวิสาหกิจ")
    start_coords = (13.7639478, 100.5355029)
    map = folium.Map(start_coords, zoom_start=14)
    for x in data:
        point = (x.latitude, x.longitude)
        folium.Marker(location=[x.latitude, x.longitude], popup=folium.Popup(x.description, max_width=400,min_width=300), tooltip=x.name).add_to(map)
        # folium.Circle(radius=5000, location=[x.latitude, x.longitude], color='crimson', fill=False,).add_to(map)

        # folium.Marker(point).add_to(map)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
    folium.raster_layers.TileLayer('CartoDB positron').add_to(map)
    folium.raster_layers.TileLayer('CartoDB dark_matter').add_to(map)
    folium.LayerControl().add_to(map)

    map = map._repr_html_()
    context = {
        'map': map,

    }

    return render(request,"maps.html", context)