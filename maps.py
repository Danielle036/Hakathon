import webbrowser
import folium
from IPython.core.display import display
from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="Geopy Library")

getLoc = loc.geocode(input("Enter location: "))
print(getLoc.latitude, getLoc.longitude)

location=[getLoc.latitude, getLoc.longitude]
m = folium.Map(location, zoom_start=18)
folium.Marker(location,tooltip='your house?').add_to(m)
m.save('map.html')
new = 2
webbrowser.open('map.html', new=new)