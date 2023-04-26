"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_maps.options.series.flowmap import (FlowmapSeries as cls,
                                                    GeoHeatmapSeries as cls2)
from highcharts_maps import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
        'data': [
            ['Point 1', 'Point 2', 4],
            ['Point 2', 'Point 3', 3]
        ]
    }, None),
    ({
        'data': [
            [[123, 456], {'lon': 123, 'lat': 456}, 4],
            ['Point 2', 'Point 3', 3]
        ]
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_FlowmapSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_FlowmapSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_FlowmapSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_FlowmapSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/flowmap/01.js', False, None),
    ('series/flowmap/02.js', False, None),

    ('series/flowmap/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/flowmap/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/flowmap/01.js', True, None),
    ('series/flowmap/02.js', True, None),

    ('series/flowmap/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/flowmap/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_FlowmapSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


##### NEXT CLASS

STANDARD_PARAMS_2 = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_GeoHeatmapSeries__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_GeoHeatmapSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_GeoHeatmapSeries_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_GeoHeatmapSeries_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/flowmap/01.js', False, None),
    ('series/flowmap/02.js', False, None),

    ('series/flowmap/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/flowmap/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/flowmap/03.js', True, None),
    ('series/flowmap/04.js', True, None),

    ('series/flowmap/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/flowmap/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_GeoHeatmapSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)
