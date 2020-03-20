# MagicSearch

<br>

![logo](https://github.com/nickprock/wRappoveRpass/blob/img/magicsearch.png)

<br>

### A simple wrapper for Overpass API download and others utils function.
This library is useful to download bus stop from OSM. Is the Python version about MagicWrap, actually is work in progress.

The main objective is to simplify the use of [Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API) to download points of interest.

The package contains other utils function like functions to switch from lat/lon to tile coordinates.

<br>

![Milano](https://github.com/nickprock/wRappoveRpass/blob/img/export.png)

<br>

### Install
1. Download .zip
2. From terminal or Anaconda prompt go into the folder where is your file
3. Write
```
pip install magicsearch-master.zip
```

### Example

```
import magicsearch as ms
ms.__version__
```

Download the bus stops in Milan
```
from magicsearch.magicwrap import poiWrapper
milan = poiWrapper(city="Milano")
my_bus_stops = milan.download()
```

### Citation
If you use my code in your research, mention this project.
```
@misc{MagicSearch,
  author =       {Nicola Procopio},
  title =        {magicsearch},
  howpublished = {\url{https://github.com/MagicBusApp/magicsearch/}},
  year =         {2020}
}
```

--------------

<a rel="license" href="https://creativecommons.org/licenses/by-sa/2.0/"><img alt="Licenza Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/2.0/88x31.png" /></a><br />Quest'opera è distribuita con Licenza <a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/">Creative Commons Attribution-ShareAlike 2.0 General</a>.
