from typing import Optional, List
from collections import UserDict

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
    """The map :term:`geometry` data which defines the areas and features of the map
    itself."""

    def __init__(self, **kwargs):
        self._force_geojson = None
        self._topology = None

        self.force_geojson = kwargs.get('force_geojsons', False)
        self.topology = kwargs.get('topology', None)

    @property
    def force_geojson(self) -> Optional[bool]:
        """If ``True``, will serialize as :term:`GeoJSON`. If ``False``, will serialize
        as :term:`TopoJSON` which sends less data over the wire. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._force_geojson

    @force_geojson.setter
    def force_geojson(self, value):
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
        if not value:
            self._topology = None
        elif isinstance(value, Topology):
            self._topology = value
        elif checkers.is_type(value, 'GeoDataFrame'):
            self._topology = Topology(value, prequantize = False)
        elif isinstance(value, (str, bytes)):
            as_dict = json.loads(value)
            if 'data' in as_dict:
                self._topology = Topology(as_dict, object_name = 'data')
            else:
                self._topology = Topology(as_dict)
        elif isinstance(value, (dict, UserDict)):
            if 'data' in as_dict:
                self._topology = Topology(as_dict, object_name = 'data')
            else:
                self._topology = Topology(as_dict)
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
            as_geojson = self.topology.to_geojson()
            as_json = geojson.dumps(as_geojson)

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
                      encoding = 'utf-8') -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        as_str = self.to_json(encoding = encoding)

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    @classmethod
    def from_js_literal(cls,
                        as_str_or_file,
                        allow_snake_case: bool = True,
                        _break_loop_on_failure: bool = False):
        """Return a Python object representation of a Highcharts JavaScript object
        literal.

        :param as_str_or_file: The JavaScript object literal, represented either as a
          :class:`str <python:str>` or as a filename which contains the JS object literal.
        :type as_str_or_file: :class:`str <python:str>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :param _break_loop_on_failure: If ``True``, will break any looping operations in
          the event of a failure. Otherwise, will attempt to repair the failure. Defaults
          to ``False``.
        :type _break_loop_on_failure: :class:`bool <python:bool>`

        :returns: A Python object representation of the Highcharts JavaScript object
          literal.
        :rtype: :class:`HighchartsMeta`
        """
        is_file = checkers.is_file(as_str_or_file)
        if is_file:
            with open(as_str_or_file, 'r') as file_:
                as_str = file_.read()
        else:
            as_str = as_str_or_file

        as_dict = json.loads(as_str)

        return cls.from_dict(as_dict,
                             allow_snake_case = allow_snake_case)

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

    def to_geodataframe(self, obj = None):
        """Generate a :class:`GeoPandas.GeoDataFrame <geopandas:GeoDataFrame>` instance
        of the :term:`map data`.

        :param obj: If the map data contains multiple objects, you can generate
          serialize a specific object by specifying its name or index. Defaults to
          :obj:`None <python:None>`, which behaves as an index of 0.
        :type obj: :class:`str <python:str>` or :class:`int <python:int>` or
          :obj:`None <python:None>`

        :rtype: :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`
        """
        return self.topology.to_gdf(object_name = obj)

    @classmethod
    def from_geodataframe(cls, as_gdf, prequantize = False):
        """Create a :class:`MapData` instance from a
        :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`.

        :param as_gdf: The :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`
          containing the :term:`map data`.
        :type as_gdf: :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`

        :param prequantize: If ``True``, will perform the TopoJSON optimizations
          ("quantizing the topology") before generating the :class:`Topology` instance.
          Defaults to ``False``.
        :type prequantize: :class:`bool <python:bool>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
        """
        topology = Topology(as_gdf, prequantize = prequantize)

        return cls(topology = topology)


class AsyncMapData(HighchartsMeta):
    """Configuration of :term:`map data` which
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
        self.fetch_counter = kwargs.get('fetch_counter', 0)

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
        """An optional (JavaScript) function which receives the :term:`map data`
        downloaded from
        :meth:`.url <highcharts_maps.options.series.data.map_data.AsyncMapData.url>`, can
        perform some (arbitrary - it's up to you!) operation on that data, and returns a
        new set of :term:`map data` which will be visualized by
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
        asynchronous ``fetch()`` call to download the :term:`map data`. Defaults to
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
        if self.url:
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
        self._fetch_counter = validators.integer(value, minimum = 0)

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
                      encoding = 'utf-8') -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

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

        if self.fetch_counter > 0:
            fetch = fetch.replace('const topology', f'const topology{self.fetch_counter}')

        as_str = f'{function}{fetch}'

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str