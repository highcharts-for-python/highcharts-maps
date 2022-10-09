from typing import Optional

from validator_collection import validators, checkers

from topojson import Topology as TopologyBase


class Topology(TopologyBase):
    """Object representation of a :term:`topology`.

    .. note::

      Inherits from :class:`topojson.Topology <topojson:Topology>` with additional
      methods conforming to the
      :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` interface.

    """

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return as_dict

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
        return cls(as_dict)

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return self.to_dict()

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

        as_json = super().to_json()

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

        return cls.from_dict(as_str)

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
        return cls.from_json(as_str_or_file,
                             allow_snake_case = allow_snake_case)

    @classmethod
    def from_geojson(cls,
                     as_geojson_or_file: str | bytes,
                     allow_snake_case: bool = True,
                     **kwargs):
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
        return cls(as_geojson_or_file, **kwargs)

    @classmethod
    def from_topojson(cls,
                      as_topojson_or_file: str | bytes,
                      allow_snake_case: bool = True,
                      **kwargs):
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
        return cls(as_topojson_or_file, **kwargs)

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
        return self.to_json(filename = filename, encoding = encoding)

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
        return self.to_gdf(object_name = obj)

    @classmethod
    def from_geodataframe(cls,
                          as_gdf,
                          prequantize = False,
                          **kwargs):
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
        return cls(as_gdf, prequantize = prequantize, **kwargs)
