import requests
import json

class poiWrapper:
    def __init__(self, city: str, tag: str = "highway", value: str = "bus_stop"):
        self.city = city
        self.tag = tag
        self.value = value
        self.url = "http://overpass-api.de/api/interpreter"
        
    def download(self):
        query = "[out:json][timeout:25]; area[name='" + self.city + "']->.a; node(area.a)['" + self.tag + "'='" + self.value + "']; out body;>;out skel qt;"
        print(query)
        response = requests.get(self.url, params={'data': query})
        data = response.json()
        return data