import folium
import opencage
import phonenumbers
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, geocoder

from phoneNumber import number

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

key="6a69c118e70c43ccadb9112a8903c180"
geocoder = OpenCageGeocode(key)
query = str(location)
results= geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)


myMap = folium.Map(location = [lat , lng] , zoom_start= 9 )
folium.Marker([lat,lng], popup=location).add_to(myMap)
myMap.save("myLocation.html")



