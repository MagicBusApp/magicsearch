"""
@date: 04/03/2020 19:36
@owner: magicbusapp
@author: Nicola Procopio
@description: a class to download point of interest from openstreetmap with overpass API
"""
import requests
import json

class poiWrapper:
    """
    A class to download point of interest in a city from openstreetmap using overpass query language and overpass api. By default downloads bus stop.

    Parameters:
    --------------
    city: str.
        The city to download data from.

    tag: str.
        default "highway". Key  used to describe a topic, category, or type of feature.

    value: str.
        default "bus_stop". The value details the specific form of the key-specified feature.

    Returns:
    --------------
    a python dict from a json, the overpass-api's response.

    Example:
    --------------
    >> from magicsearch.magicwrap import poiWrapper
    >> milano_bus_stops = poiWrapper("Milano").download()

    References:
    --------------
    The official page about openstreetmap tags [https://wiki.openstreetmap.org/wiki/Tags]
    """
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