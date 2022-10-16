"""Tests for ``highcharts.no_data``."""

import pytest

import datetime
from json.decoder import JSONDecodeError

from highcharts_maps.options.series.data.map_data import (MapData as cls,
                                                          AsyncMapData as cls2)
from highcharts_maps import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal_with_expected, Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_MapData__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_MapData__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_MapData_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_MapData_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, expected_filename, as_file, error', [
    ('series/data/map_data/map_data/01.js',
     'series/data/map_data/map_data/world.topo.json',
     False,
     None),
    ('series/data/map_data/map_data/02.js',
     'series/data/map_data/map_data/world.topo.json',
     False,
     None),

    ('series/data/map_data/map_data/error-01.js',
     'series/data/map_data/map_data/world.topo.json',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    # As GeoJSON
    ('series/data/map_data/map_data/03.js',
     'series/data/map_data/map_data/world.geo.json',
     False,
     None),

])
def test_MapData_from_js_literal(input_files,
                                 filename,
                                 expected_filename,
                                 as_file,
                                 error):
    Class_from_js_literal_with_expected(cls,
                                        input_files,
                                        filename,
                                        expected_filename,
                                        as_file,
                                        error)

###### Next Class

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_AsyncMapData__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_AsyncMapData__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_AsyncMapData_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_AsyncMapData_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)

@pytest.mark.parametrize('filename, expected_filename, as_file, error', [
    ('series/data/map_data/async_map_data/01-input.js',
     'series/data/map_data/async_map_data/01-expected.js',
     False,
     None),

])
def test_AsyncMapData_from_js_literal(input_files,
                                      filename,
                                      expected_filename,
                                      as_file,
                                      error):
    Class_from_js_literal_with_expected(cls2,
                                        input_files,
                                        filename,
                                        expected_filename,
                                        as_file,
                                        error)
