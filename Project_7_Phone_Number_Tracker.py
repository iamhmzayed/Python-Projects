#Project_7_Phone_Number_Tracker

import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import folium

from opencage.geocoder import OpenCageGeocode

# Get the API key from OpenCage Geocoder
api_key = "6b1c8b12457f4b5caeec3644a4c5d386"
geocoder_service = OpenCageGeocode(api_key)

def track_phone_number(phone_number):
    # Parse the phone number
    phoneNumber = phonenumbers.parse(phone_number)

    # Get the timezone
    timeZone = timezone.time_zones_for_number(phoneNumber)
    print("Timezone:", timeZone)

    # Get the geolocation
    geolocation = geocoder.description_for_number(phoneNumber, 'en')
    print("Geolocation:", geolocation)

    # Get the carrier
    carrierName = carrier.name_for_number(phoneNumber, 'en')
    print("Carrier:", carrierName)

    # Get the exact country, city, and place using OpenCage Geocoder
    query = f"{geolocation}"
    results = geocoder_service.geocode(query)
    if results and len(results) > 0:
        result = results[0]
        print("Country:", result['components'].get('country', 'N/A'))
        print("City:", result['components'].get('city', 'N/A'))
        print("Place:", result['formatted'])

        # Create a Folium map to display the location
        map = folium.Map(location=[result['geometry']['lat'], result['geometry']['lng']], zoom_start=10)
        folium.Marker([result['geometry']['lat'], result['geometry']['lng']], popup=f"{phoneNumber.national_number} {phoneNumber.country_code}").add_to(map)
        map.save("phone_number_location.html")
    else:
        print("No results found for the given phone number.")

# Test the function
track_phone_number("01879944516")
