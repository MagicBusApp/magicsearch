from setuptools import setup

exec(open('magicsearch/version.py').read())
setup(
   name='magicsearch',
   version=__version__,
   description='A python wrapper for Overpass API. Search the bus stop (or other points of interest) in a city and download in json format.',
   license="LICENSE.txt",
   long_description=open('README.md').read(),
   author='Nicola Procopio',
   url="https://github.com/MagicBusApp/",
   packages=['magicsearch'],  #same as name
   install_requires=['requests'], #external packages as dependencies
)
