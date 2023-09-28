from typing import Optional
from collections import UserDict
import requests
import os

try:
    import orjson as json
except ImportError:
    try:
        import rapidjson as json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            import json

import geojson
from validator_collection import validators, checkers

from highcharts_maps import errors, utility_functions
from highcharts_maps.decorators import class_sensitive
from highcharts_maps.metaclasses import HighchartsMeta
from highcharts_maps.utility_classes.topojson import Topology
from highcharts_maps.utility_classes.javascript_functions import CallbackFunction
from highcharts_maps.utility_classes.fetch_configuration import FetchConfiguration


class MapData(HighchartsMeta):
    """The :term:`map geometry` data which defines the areas and features of the map
    itself."""

    def __init__(self, **kwargs):
        self._force_geojson = None
        self._topology = None

        self.force_geojson = kwargs.get('force_geojsons', None)
        self.topology = kwargs.get('topology', None)

    def __str__(self):
        """Return a human-readable :class:`str <python:str>` representation of the map 
        data.

        .. warning::
        
          To ensure that the result is human-readable, the result will be rendered
          *without* its 
          :meth:`.topology <highcharts_maps.options.series.data.map_data.MapData.topology>`
          property.
        
          .. tip::
        
            If you would like a *complete* and *unambiguous* :class:`str <python:str>` 
            representation, then you can:
            
            * use the 
              :meth:`__repr__() <highcharts_maps.options.series.data.map_data.MapData.__repr__>` method,
            * call ``repr(my_map_data)``, or
            * serialize the chart to TopoJSON using 
              :meth:`.to_topojson() <highcharts_maps.options.series.data.map_data.MapData.to_topojson>`
            * serialize the chart to GeoJSON using 
              :meth:`.to_geojson() <highcharts_maps.options.series.data.map_data.MapData.to_geojson>`
            
        :returns: A :class:`str <python:str>` representation of the map data.
        :rtype: :class:`str <python:str>`
        """
        as_dict = self.to_dict()

        kwargs = {utility_functions.to_snake_case(key): as_dict[key]
                  for key in as_dict if key not in ['topology']}
        kwargs_as_str = ', '.join([f'{key} = {repr(kwargs[key])}'
                                   for key in kwargs])

        return f'{self.__class__.__name__}({kwargs_as_str})'

    @property
    def force_geojson(self) -> Optional[bool]:
        """If ``True``, will serialize as :term:`GeoJSON`. If ``False``, will serialize
        as :term:`TopoJSON` which sends less data over the wire. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._force_geojson

    @force_geojson.setter
    def force_geojson(self, value):
        if value is None:
            self._force_geojson = None
        else:
            self._force_geojson = bool(value)

    @property
    def topology(self) -> Optional[Topology]:
        """The :term:`topology` that defines the map areas that should be rendered in the
        map.

        :rtype: :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>`
        """
        return self._topology

    @topology.setter
    def topology(self, value):
        is_file = checkers.is_file(value)
        if not is_file and isinstance(value, (str, bytes)):
            try:
                value_as_path = os.path.abspath(value)
                is_file = os.path.isfile(value_as_path)
                if is_file:
                    value = value_as_path
            except TypeError:
                is_file = False

        if not value:
            self._topology = None
        elif is_file:
            with open(value, 'r') as as_file:
                try:
                    as_dict = json.load(as_file)
                except AttributeError:
                    as_str = as_file.read()
                    as_dict = json.loads(as_str)

            if 'data' in as_dict.get('objects', {}):
                self._topology = Topology(as_dict, object_name = 'data')
            elif 'default' in as_dict.get('objects', {}):
                self._topology = Topology(as_dict, object_name = 'default')
            else:
                self._topology = Topology(as_dict)

        elif checkers.is_url(value):
            request = requests.get(value)
            request.raise_for_status()
            as_dict = json.loads(request.content)

            if 'data' in as_dict.get('objects', {}):
                self._topology = Topology(as_dict, object_name = 'data')
            elif 'default' in as_dict.get('objects', {}):
                self._topology = Topology(as_dict, object_name = 'default')
            else:
                self._topology = Topology(as_dict)
        elif isinstance(value, Topology):
            self._topology = value
        elif checkers.is_type(value, 'GeoDataFrame'):
            self._topology = Topology(value, prequantize = False)
        elif isinstance(value, (str, bytes)):
            if '"data"' in value:
                self._topology = Topology(value, object_name = 'data')
            elif '"default"' in value:
                self._topology = Topology(value, object_name = 'default')
            else:
                try:
                    as_dict = json.load(value)
                except AttributeError:
                    as_dict = json.loads(value)

            if 'data' in as_dict.get('objects', {}):
                self._topology = Topology(as_dict, object_name = 'data')
            elif 'default' in as_dict.get('objects', {}):
                self._topology = Topology(as_dict, object_name = 'default')
            else:
                self._topology = Topology(as_dict)
        elif isinstance(value, (dict, UserDict)):
            if 'data' in value.get('objects', {}):
                self._topology = Topology(value, object_name = 'data')
            elif 'default' in value.get('objects', {}):
                self._topology = Topology(value, object_name = 'default')
            else:
                self._topology = Topology(value)
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
            data = []
            object_names = []
            is_GeoDataFrame = False
            for count, item in enumerate(value):
                data.append(item)
                object_names.append(f'obj_{count}')
                if checkers.is_type(item, 'GeoDataFrame'):
                    is_GeoDataFrame = True
            if is_GeoDataFrame:
                self._topology = Topology(data = data,
                                          object_name = object_names,
                                          prequantize = False)
            else:
                self._topology = Topology(data = data,
                                          object_name = object_names)
        else:
            try:
                self._topology = Topology(value)
            except (json.JSONDecodeError, ValueError, TypeError):
                raise errors.HighchartsValueError(f'Unable to deserialize a topology from'
                                                  f' the value supplied: {value}')

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        if ('forceGeoJSON' in as_dict
            or 'force_geojson' in as_dict
            or 'topology' in as_dict):
            kwargs = {
                'force_geojson': as_dict.get('force_geojson',
                                             as_dict.get('forceGeoJSON', False)),
                'topology': as_dict.get('topology', None),
            }
        else:
            kwargs = {
                'topology': as_dict
            }

        return kwargs

    @classmethod
    def from_dict(cls,
                  as_dict: dict,
                  allow_snake_case: bool = True):
        """Construct an instance of the class from a :class:`dict <python:dict>` object.

        :param as_dict: A :class:`dict <python:dict>` representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python object representation of ``as_dict``.
        :rtype: :class:`HighchartsMeta`
        """
        as_dict = validators.dict(as_dict, allow_empty = True) or {}
        if ('forceGeoJSON' in as_dict or 'force_geojson' in as_dict
            or ('topology' in as_dict and len(as_dict) == 1)):
            clean_as_dict = {}
            for key in as_dict:
                if allow_snake_case:
                    clean_key = utility_functions.to_camelCase(key)
                else:
                    clean_key = key

                clean_as_dict[clean_key] = as_dict[key]

            kwargs = cls._get_kwargs_from_dict(clean_as_dict)
        else:
            kwargs = {
                'topology': as_dict
            }

        return cls(**kwargs)

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'forceGeoJSON': self.force_geojson,
            'topology': self.topology
        }

        return untrimmed

    def to_json(self,
                filename = None,
                encoding = 'utf-8'):
        """Generate a JSON string/byte string representation of the object compatible with
        the Highcharts JavaScript library.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A JSON representation of the object compatible with the Highcharts
          library.
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        if filename:
            filename = validators.path(filename)

        if not self.force_geojson:
            as_json = self.topology.to_json()
        else:
            as_json = self.topology.to_geojson()

        if filename:
            if isinstance(as_json, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_json)

        return as_json

    @classmethod
    def from_json(cls,
                  as_json_or_file: str | bytes,
                  allow_snake_case: bool = True):
        """Construct an instance of the class from a JSON string.

        :param as_json_or_file: The JSON string for the object or the filename of a file
          that contains the JSON string.
        :type as_jsonor_file: :class:`str <python:str>` or :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_json``.
        :rtype: :class:`MapData`
        """
        is_file = checkers.is_file(as_json_or_file)
        if is_file:
            with open(as_json_or_file, 'r') as file_:
                as_str = file_.read()
        else:
            as_str = as_json_or_file

        as_dict = json.loads(as_str)

        return cls.from_dict(as_dict,
                             allow_snake_case = allow_snake_case)

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8',
                      careful_validation = False) -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :param careful_validation: if ``True``, will carefully validate JavaScript values
        along the way using the
        `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
        to ``False``.
        
        .. warning::
        
            Setting this value to ``True`` will significantly degrade serialization
            performance, though it may prove useful for debugging purposes.

        :type careful_validation: :class:`bool <python:bool>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        as_json = self.to_json(encoding = encoding)

        if filename:
            if isinstance(as_json, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_json)

        return as_json

    def to_geojson(self,
                   filename = None,
                   encoding = 'utf-8'):
        """Generate a :term:`GeoJSON` string/byte string representation of the object.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A :term:`GeoJSON` representation of the object
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        if filename:
            filename = validators.path(filename)

        as_geojson = self.topology.to_geojson()

        if filename:
            if isinstance(as_geojson, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_geojson)

        return as_geojson

    @classmethod
    def from_geojson(cls,
                     as_geojson_or_file: str | bytes,
                     allow_snake_case: bool = True):
        """Construct an instance of the class from a JSON string.

        :param as_geojson_or_file: The :term:`GeoJSON` string for the object or the
          filename of a file that contains the GeoJSON string.
        :type as_geojson_or_file: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_geojson_or_file``.
        :rtype: :class:`MapData`
        """
        return cls.from_json(as_geojson_or_file, allow_snake_case = allow_snake_case)

    def to_topojson(self,
                    filename = None,
                    encoding = 'utf-8'):
        """Generate a :term:`TopoJSON` string/byte string representation of the object.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A :term:`TopoJSON` representation of the object
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        if filename:
            filename = validators.path(filename)

        as_topojson = self.topology.to_json()

        if filename:
            if isinstance(as_topojson, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_topojson)

        return as_topojson

    @classmethod
    def from_topojson(cls,
                      as_topojson_or_file: str | bytes,
                      allow_snake_case: bool = True):
        """Construct an instance of the class from a :term:`TopoJSON` string.

        :param as_topojson_or_file: The :term:`TopoJSON` string for the object or the
          filename of a file that contains the TopoJSON string.
        :type as_topojson_or_file: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_topojson_or_file``.
        :rtype: :class:`MapData`
        """
        return cls.from_json(as_topojson_or_file, allow_snake_case = allow_snake_case)

    def to_geodataframe(self, object_name = None):
        """Generate a :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>` instance
        of the :term:`map geometry`.

        :param object_name: If the map data contains multiple objects, you can generate
          serialize a specific object by specifying its name or index. Defaults to
          :obj:`None <python:None>`, which behaves as an index of 0.
        :type object_name: :class:`str <python:str>` or :class:`int <python:int>` or
          :obj:`None <python:None>`

        :rtype: :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`
        """
        return self.topology.to_gdf(object_name = object_name)

    @classmethod
    def from_geodataframe(cls, as_gdf, prequantize = False, **kwargs):
        """Create a :class:`MapData` instance from a
        :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`.

        :param as_gdf: The :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`
          containing the :term:`map geometry`.
        :type as_gdf: :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`

        :param prequantize: If ``True``, will perform the TopoJSON optimizations
          ("quantizing the topology") before generating the :class:`Topology` instance.
          Defaults to ``False``.
        :type prequantize: :class:`bool <python:bool>`
        
        :param kwargs: additional keyword arguments which are passed to the
          :class:`Topology` constructor
        :type kwargs: :class:`dict <python:dict>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
        """
        topology = Topology(as_gdf, prequantize = prequantize, **kwargs)

        return cls(topology = topology)

    @classmethod
    def from_shapefile(cls, shp_filename):
        """Create a :class:`MapData` instance from an :term:`ESRI Shapefile <shapefile>`.

        :param shp_filename: The full filename of an :term:`ESRI Shapefile <shapefile>`
          to load.

          .. note::

            :term:`ESRI Shapefiles <shapefile>` are actually composed of three files each,
            with one file receiving the ``.shp`` extension, one with a ``.dbf`` extension,
            and one (optional) file with a ``.shx`` extension.

            **Highcharts Maps for Python** will resolve all three files given a single
            base filename. Thus:

              ``/my-shapefiles-folder/my_shapefile.shp``

            will successfully load data from the three files:

              ``/my-shapefiles-folder/my_shapefile.shp``
              ``/my-shapefiles-folder/my_shapefile.dbf``
              ``/my-shapefiles-folder/my_shapefile.shx``

          .. tip::

            **Highcharts for Python** will also correctly load and unpack
            :term:`shapefiles <shapefile>` that are grouped together within a ZIP file.

        :type shp_filename: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
        """
        try:
            import shapefile
        except ImportError:
            raise errors.HighchartsDependencyError('MapSeriesBase.from_shapefile() '
                                                   'requires PyShp be installed. '
                                                   'However, it was not found in the '
                                                   'runtime environment.')

        shp_filename = validators.file_exists(shp_filename)

        data = shapefile.Reader(shp_filename)

        topology = Topology(data)

        return cls(topology = topology)


class AsyncMapData(HighchartsMeta):
    """Configuration of :term:`map geometry` which
    `Highcharts Maps <https://www.highcharts.com/products/maps>`__ should fetch
    *asynchronously* using client-side JavaScript.

    .. note::

      When serialized to a JS literal will execute an async (JavaScript) ``fetch()`` call
      to download the map data from
      :meth:`.url <highcharts_maps.options.series.data.map_data.AsyncMapData.url>`.

    """

    def __init__(self, **kwargs):
        self._url = None
        self._selector = None
        self._fetch_config = None
        self._fetch_counter = None

        self.url = kwargs.get('url', None)
        self.selector = kwargs.get('selector', None)
        self.fetch_config = kwargs.get('fetch_config', None)
        self.fetch_counter = kwargs.get('fetch_counter', None)

    @property
    def url(self) -> Optional[str]:
        """The URL that the (JavaScript) ``fetch()`` function will be requesting, which
        should return either :term:`TopoJSON` or :term:`GeoJSON` data. Defaults to
        :obj:`None <python:None>`.

        .. note::

          This property will *overwrite* any URL configured within
          :meth:`.fetch_config <highcharts_maps.options.series.data.map_data.AsyncMapData.fetch_config>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._url

    @url.setter
    def url(self, value):
        self._url = validators.url(value, allow_empty = True)

    @property
    def selector(self) -> Optional[CallbackFunction]:
        """An optional (JavaScript) function which receives the :term:`map geometry`
        downloaded from
        :meth:`.url <highcharts_maps.options.series.data.map_data.AsyncMapData.url>`, can
        perform some (arbitrary - it's up to you!) operation on that data, and returns a
        new set of :term:`map geometries <map geometry>` which will be visualized by
        `Highcharts for Maps <https://www.highcharts.com/products/maps/>`__. Defaults to
        :obj:`None <python:None>`.

        .. note::

          The ``selector`` function *must* accept a single argument: ``topology`` and
          *must* return a single value (which will be assigned to the JavaScript variable
          named ``topology``).

        :rtype: :class:`CallbackFunction <highcharts_maps.utility_classes.javascript_functions.CallbackFunction>`
          or :obj:`None <python:None>`
        """
        return self._selector

    @selector.setter
    @class_sensitive(CallbackFunction)
    def selector(self, value):
        self._selector = value

    @property
    def fetch_config(self) -> Optional[FetchConfiguration]:
        """Optional configuration settings to use when executing the (JavaScript)
        asynchronous ``fetch()`` call to download the :term:`map geometry`. Defaults to
        :obj:`None <python:None>`.

        .. note::

          The :meth:`.url <highcharts_maps.options.series.data.map_data.AsyncMapData.url>`.
          setting will override any URL set in the
          :class:`FetchConfiguration <highcharts_maps.utility_classes.fetch_configuration.FetchConfiguration>`.

        :rtype: :class:`FetchConfiguration <highcharts_maps.utility_classes.fetch_configuration.FetchConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._fetch_config

    @fetch_config.setter
    @class_sensitive(FetchConfiguration)
    def fetch_config(self, value):
        self._fetch_config = value
        if not self._fetch_config and self.url:
            self._fetch_config = FetchConfiguration(url = self.url)
        elif self.url:
            self.fetch_config.url = self.url

    @property
    def fetch_counter(self) -> int:
        """The number to append to the ``topology`` variable name when serializing the
        map data. Defaults to ``0``.

        :rtype: :class:`int <python:int>`
        """
        return self._fetch_counter

    @fetch_counter.setter
    def fetch_counter(self, value):
        self._fetch_counter = validators.integer(value, allow_empty = True, minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'url': as_dict.get('url', None),
            'selector': as_dict.get('selector', None),
            'fetch_config': as_dict.get('fetchConfig', as_dict.get('fetch_config', None)),
            'fetch_counter': as_dict.get('fetchCounter',
                                         as_dict.get('fetch_counter', None)),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'url': self.url,
            'selector': self.selector,
            'fetchConfig': self.fetch_config,
            'fetchCounter': self.fetch_counter,
        }

        return untrimmed

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8',
                      careful_validation = False) -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :param careful_validation: if ``True``, will carefully validate JavaScript values
        along the way using the
        `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
        to ``False``.
        
        .. warning::
        
            Setting this value to ``True`` will significantly degrade serialization
            performance, though it may prove useful for debugging purposes.

        :type careful_validation: :class:`bool <python:bool>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        if self.fetch_config:
            self.fetch_config.url = self.url
            fetch_config = self.fetch_config
        else:
            fetch_config = FetchConfiguration(self.url)
            
        if self.selector:
            function = f"""const selector = {str(self.selector)};\n"""
            fetch = f"""const topology = await {str(fetch_config)}.then(response => selector(response.json()));"""
        else:
            function = ''
            fetch = f"""const topology = await {str(fetch_config)}.then(response => response.json());"""

        if self.fetch_counter and self.fetch_counter > 0:
            fetch = fetch.replace('const topology', f'const topology{self.fetch_counter}')

        as_str = f'{function}{fetch}'

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str
