import webbrowser
import folium
from IPython.core.display import display
from geopy.geocoders import Nominatim

def get_geolocation(address):
    loc = Nominatim(user_agent="Geopy Library")
    get_loc = loc.geocode(address)
    return [get_loc.latitude, get_loc.longitude]

def add_markers(m, restaurants):
    for address in restaurants:
        text=f"""name: {restaurants[address][0]}
        kosher: {restaurants[address][1]}
        consept: {restaurants[address][2]}
        link: 
        """
        folium.Marker(get_geolocation(address), popup=f"{text}<a href={restaurants[address][3]}>website</a>").add_to(m)


def create_map(location, restaurants):
    m = folium.Map(get_geolocation(location), zoom_start=18)
    add_markers(m, restaurants)
    m.save('map.html')
    new = 2
    webbrowser.open('map.html', new=new)