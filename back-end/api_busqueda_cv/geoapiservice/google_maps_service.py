import googlemaps

class GoogleMapsGeocoder:
    def __init__(self, api_key):
        self.gmaps = googlemaps.Client(key=api_key)

    def getlatlong(self, address):
        geocode_result = self.gmaps.geocode(address)
        if geocode_result and len(geocode_result) > 0:
            latitude = geocode_result[0]['geometry']['location']['lat']
            longitude = geocode_result[0]['geometry']['location']['lng']
            return latitude, longitude
        else:
            return None, None
