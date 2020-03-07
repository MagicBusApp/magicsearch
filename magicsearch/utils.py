"""
@date: 04/03/2020 20:52
@owner: magicbusapp
@author: Nicola Procopio
@description: functions to convert lat/lon to tile and the other way around
"""
import math

def deg2num(lat_deg, lon_deg, zoom):
    """
    Transform coordinates lat/lon to tiles x/y

    Parameters:
    --------------
    lat_deg: float.
        latitude
    
    lon_deg: float.
        longitude
    
    zoom: int.
        zoom of the map. From 0 to 19.
    
    Returns:
    --------------
    a vector with x and y coordinates about tile center.

    Exemple:
    --------------
    >> from magicsearch.utils import deg2num
    >> deg2num(39.164, 16.224, 18)

    References:
    ---------------
    https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Pseudo-code
    """
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (xtile, ytile)

def num2deg(xtile, ytile, zoom):
    """
    Transform x/y tile center in lat/lon coordinates

    Parameters:
    --------------
    xtile: float.
        x coordinate to the tile center
    
    ytile: float.
        y coordinate to the tile center
    
    zoom: int.
        zoom of the map. From 0 to 19.
    
    Returns:
    --------------
    a vector with lat and lon.

    Exemple:
    --------------
    >> from magicsearch.utils import num2deg
    >> num2deg(63, 42, 7)

    References:
    ---------------
    https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Pseudo-code
    """
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)