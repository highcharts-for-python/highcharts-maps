"""Defines a set of constants that are used throughout the library."""
from highcharts_core.constants import *


MAPS_INCLUDE_LIBS = INCLUDE_LIBS + [
    'https://code.highcharts.com/maps/modules/map.js'
]

MAPS_INCLUDE_STR = INCLUDE_STR + """
    <script src="https://code.highcharts.com/maps/modules/map.js"/>
"""