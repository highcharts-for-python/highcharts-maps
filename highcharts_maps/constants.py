"""Defines a set of constants that are used throughout the library."""
from highcharts_core.constants import *

MAPS_INCLUDE_LIBS = [x for x in INCLUDE_LIBS if x != 'https://code.highcharts.com/modules/heatmap.js']
MAPS_INCLUDE_LIBS.extend([
    'https://code.highcharts.com/maps/modules/map.js',
    'https://code.highcharts.com/maps/modules/flowmap.js',
    'https://code.highcharts.com/maps/modules/geoheatmap.js',
])

MAPS_INCLUDE_STR = INCLUDE_STR + """
    <script src="https://code.highcharts.com/maps/modules/map.js"/>
    <script src="https://code.highcharts.com/maps/modules/flowmap.js"/>
    <script src="https://code.highcharts.com/maps/modules/geoheatmap.js"/>
"""