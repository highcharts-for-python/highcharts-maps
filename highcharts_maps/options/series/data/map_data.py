from typing import Optional, List
from collections import UserDict

from validator_collection import validators, checkers

from highcharts_maps import errors
from highcharts_maps.decorators import validate_types
from highcharts_maps.metaclasses import HighchartsMeta
from highcharts_maps.utility_classes.geojson import GeoJSON
from highcharts_maps.utility_classes.topojson import TopoJSON


class MapData(HighchartsMeta):
    """Map :term:`geometries` that provide instructions on how to render the map
    itself, along with relevant properties used to join each map area to its
    corresponding values in the series
    :meth:`.data <highcharts_maps.options.series.base.MapSeriesBase.data>`.

    .. warning::

      To minimize data transferred on the wire, all geometries supplied in :term:`GeoJSON`
      will be automatically converted to :term:`TopoJSON` (which is a significantly more
      efficient/compact format). If your JavaScript code *needs* to have the data
      delivered in JSON, set
      :meth:`.force_geojson <highcharts_maps.options.series.data.map_data.MapData.force_geojson>`
      to ``True``.

    .. tip::

      **Best practice!**

      Because :iabbr:`GIS (Geograhical Information System)` :term:`geometries` can be
      verbose and large, we strongly recommend fetching geometry data asynchronously from
      the client-side. **Highcharts for Maps** supports asynchronously-fetched map data
      using the
      :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
      class instead of the
      :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`.

    """

    def __init__(self, **kwargs):
        self._as_geojson = None
        self._as_topojson = None
        self._defer_conversion = None
        self._force_geojson = None

        self.defer_conversion = kwargs.get('defer_conversion', False)
        self.force_geojson = kwargs.get('force_geojson', False)
        self.geometries = kwargs.get('geometries', None)

    def _validate_geometry(self, value):
        """Validate that ``value`` is a valid geometry, returning the :term:`GeoJSON`
        and :term:`TopoJSON` representation.

        :param value: the value to validate as a valid :term:`geometry <geometries>`.

        :rtype: 2-member :class:`tuple <python:tuple>` where the first is
          :class:`GeoJSON <highcharts_maps.utility_classes.geojson.GeoJSON>` and the
          second is :class:`TopoJSON <highcharts_maps.utility_classes.topojson.TopoJSON>`
        """
        as_geojson = None
        as_topojson = None
        try:
            as_geojson = validate_types(value, GeoJSON)
            if not self.defer_conversion:
                as_topojson = TopoJSON.from_geojson(as_geojson)
        except (ValueError, TypeError):
            as_topojson = validate_types(value, TopoJSON)
            if self.force_geojson and not self.defer_conversion:
                as_geojson = as_topojson.to_geojson()
            else:
                as_geojson = None

        return as_geojson, as_topojson

    @property
    def force_geojson(self) -> Optional[bool]:
        """If ``True``, will always serialize the instance to :term:`GeoJSON`. If
        ``False``, will serialize the instance to :term:`TopoJSON` to minimize the amount
        of data transferred on the wire. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._force_geojson

    @force_geojson.setter
    def force_geojson(self, value):
        self._force_geojson = bool(value)

    @property
    def defer_conversion(self) -> Optional[bool]:
        """If ``True``, will defer converting :term:`GeoJSON` :term:`geometries` to
        :term:`TopoJSON` until the moment geometries are requested. This has the effect
        of avoiding an "expensive" action (in terms of performance) until it is absolutely
        necessary and only performing that action once. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._defer_conversion

    @defer_conversion.setter
    def defer_conversion(self, value):
        self._defer_conversion = bool(value)

    @property
    def geometries(self) -> Optional[TopoJSON | List[TopoJSON]]:
        """Collection of the :term:`TopoJSON` :term:`geometries` supplied in the map data.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`TopoJSON <highcharts_maps.utility_classes.topojson.TopoJSON>` or
          :class:`list <python:list>` of
          :class:`TopoJSON <highcharts_maps.utility_classes.topojson.TopoJSON>`, or
          :obj:`None <python:None>`
        """
        if self._as_geojson and not self._as_topojson:
            self._as_topojson = TopoJSON.from_geojson(self._as_geojson)

        return self._as_topojson

    @geometries.setter
    def geometries(self, value):
        if not value:
            self._as_geojson = None
            self._as_topojson = None
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
            as_geojson = []
            as_topojson = []
            for item in value:
                item_as_geojson, item_as_topojson = self._validate_geometry(item)
                if item_as_geojson:
                    as_geojson.append(item)
                if item_as_topojson:
                    as_topojson.append(item)
            if as_geojson:
                self._as_geojson = [x for x in as_geojson]
            if as_topojson:
                self._as_topojson = [x for x in as_topojson]
        else:
            self._as_geojson, self._as_topojson = self._validate_geometry(value)

    @classmethod
    def from_geojson(cls,
                     as_geojson_or_file: str | bytes,
                     force_geojson: bool = False,
                     defer_conversion: bool = False):
        """Construct an instance of the :class:`MapData` from a GeoJSON string.

        :param as_geojson_or_file: The :term:`GeoJSON` string for the object or the
          filename of a file that contains the GeoJSON string.
        :type as_geojson_or_file: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :param force_geojson: If ``True``, will force the :class:`MapData` instance to be
          serialized back to :term:`GeoJSON`. If ``False``, the :term:`GeoJSON` will be
          automatically converted to :term:`TopoJSON` to limit data on the wire. Defaults
          to ``False``.
        :type force_geojson: :class:`bool <python:bool>`

        :param defer_conversion: If ``True``, will defer converting from :term:`GeoJSON`
          to :term:`TopoJSON` until the last moment before serialization. This can provide
          performance benefits and is particularly useful if you will not need to
          manipulate the map data within Python. Defaults to ``False``.
        :type defer_conversion: :class:`bool <python:bool>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
        """
        as_geojson = GeoJSON.from_json(as_geojson_or_file)

        return cls(force_geojson = force_geojson,
                   defer_conversion = defer_conversion,
                   geometries = as_geojson)

    def to_geojson(self,
                   filename = None,
                   encoding = 'utf-8'):
        """Generate a :term:`GeoJSON` string/byte string representation of the object.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A :term:`GeoJSON` representation of the object.
        :rtype: :class:`GeoJSON <highcharts_maps.utility_classes.geojson.GeoJSON>` or
          :obj:`None <python:None>`
        """
        if not self._as_geojson and not self._as_topojson:
            return None

        if not self._as_geojson and self._as_topojson:
            self._as_geojson = self._as_topojson.to_geojson()

        as_json = self._as_geojson.to_json(encoding = encoding)

        if filename:
            if isinstance(as_json, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_json)

        return self._as_geojson

    @classmethod
    def from_topojson(cls,
                      as_topojson_or_file: str | bytes,
                      force_geojson: bool = False,
                      defer_conversion: bool = False):
        """Construct an instance of the :class:`MapData` from a :term:`TopoJSON` string.

        :param as_topojson_or_file: The :term:`TopoJSON` string for the object or the
          filename of a file that contains the TopoJSON string.
        :type as_topojson_or_file: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :param force_geojson: If ``True``, will force the :class:`MapData` instance to be
          serialized back to :term:`GeoJSON`. Data wlil be serialized back to
          :term:`TopoJSON` to limit data on the wire. Defaults to ``False``.
        :type force_geojson: :class:`bool <python:bool>`

        :param defer_conversion: If ``True``, will defer converting from :term:`TopoJSON`
          to :term:`GeoJSON` (if necessary) until the last moment before serialization.
          This can provide performance benefits and is particularly useful if you will not
          need to manipulate the map data within Python. Defaults to ``False``.
        :type defer_conversion: :class:`bool <python:bool>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
        """
        as_topojson = TopoJSON.from_json(as_topojson_or_file)

        return cls(force_geojson = force_geojson,
                   defer_conversion = defer_conversion,
                   geometries = as_topojson)

    def to_topojson(self,
                    filename = None,
                    encoding = 'utf-8'):
        """Generate a :term:`TopoJSON` string/byte string representation of the object.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A :term:`GeoJSON` representation of the object.
        :rtype: :class:`TopoJSON <highcharts_maps.utility_classes.topojson.TopoJSON>` or
          :obj:`None <python:None>`
        """
        if not self._as_topojson and not self._as_geojson:
            return None

        if not self._as_topojson and self._as_geojson:
            self._as_topojson = self._as_geojson.to_topojson()

        as_json = self._as_topojson.to_json(encoding = encoding)

        if filename:
            if isinstance(as_json, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_json)

        return self._as_topojson

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'force_geojson': self.force_geojson,
            'defer_conversion': self.defer_conversion,
            'geometries': self.geometries
        }

        return untrimmed

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'force_geojson': as_dict.get('force_geojson', None),
            'defer_conversion': as_dict.get('defer_conversion', None),
            'geometries': as_dict.get('geometries', None),
        }

        return kwargs

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8') -> Optional[str]:
        """Return the object as either a :term:`TopoJSON` JavaScript object or as a
        :term:`GeoJSON` JavaScript object.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        .. note::

          If :meth:`.force_geojson <highcharts_maps.options.series.data.map_data.MapData.force_geojson>`
          is ``True``, will serialize to a :term:`GeoJSON` object. Otherwise, will
          serialize to a :term:`TopoJSON` object.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        if self._as_geojson and self.force_geojson:
            as_str = self._as_geojson.to_js_literal(encoding = encoding)
        elif self.force_geojson and self._as_topojson:
            self._as_geojson = self._as_topojson.to_geojson()
            as_str = self._as_geojson.to_js_literal(encoding = encoding)
        elif self._as_geojson and not self._as_topojson:
            self._as_topojson = TopoJSON.from_geojson(self._as_geojson)
            as_str = self._as_topojson.to_js_literal(encoding = encoding)
        elif self._as_topojson:
            as_str = self._as_topojson.to_js_literal(encoding = encoding)

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

        return cls(geometries = as_str)

    @classmethod
    def _copy_dict_key(cls,
                       key,
                       original,
                       other,
                       overwrite = True,
                       **kwargs):
        """Copies the value of ``key`` from ``original`` to ``other``.

        :param key: The key that is to be copied.
        :type key: :class:`str <python:str>`

        :param original: The original :class:`dict <python:dict>` from which it should
          be copied.
        :type original: :class:`dict <python:dict>`

        :param other: The :class:`dict <python:dict>` to which it should be copied.
        :type other: :class:`dict <python:dict>`

        :returns: The value that should be placed in ``other`` for ``key``.
        """
        original_value = original[key]
        other_value = other.get(key, None)

        if isinstance(original_value, (dict, UserDict)):
            new_value = {}
            for subkey in original_value:
                new_key_value = cls._copy_dict_key(subkey,
                                                   original_value,
                                                   other_value,
                                                   overwrite = overwrite,
                                                   **kwargs)
                new_value[subkey] = new_key_value

            return new_value

        elif checkers.is_iterable(original_value,
                                  forbid_literals = (str,
                                                     bytes,
                                                     dict,
                                                     UserDict)):
            if overwrite:
                new_value = [x for x in original_value]

                return new_value
            else:
                return other_value

        elif other_value and not overwrite:
            return other_value
        else:
            return original_value

    def copy(self,
             other = None,
             overwrite = True,
             **kwargs):
        """Copy the configuration settings from this instance to the ``other`` instance.

        :param other: The target instance to which the properties of this instance should
          be copied. If :obj:`None <python:None>`, will create a new instance and populate
          it with properties copied from ``self``. Defaults to :obj:`None <python:None>`.
        :type other: :class:`HighchartsMeta`

        :param overwrite: if ``True``, properties in ``other`` that are already set will
          be overwritten by their counterparts in ``self``. Defaults to ``True``.
        :type overwrite: :class:`bool <python:bool>`

        :param kwargs: Additional keyword arguments. Some special descendents of
          :class:`HighchartsMeta` may have special implementations of this method which
          rely on additional keyword arguments.

        :returns: A mutated version of ``other`` with new property values

        """
        if not other:
            other = self.__class__()

        if not isinstance(other, self.__class__):
            raise errors.HighchartsValueError(f'other is expected to be a '
                                              f'{self.__class__.__name__} instance. Was: '
                                              f'{other.__class__.__name__}')

        self_as_dict = self.to_dict()
        other_as_dict = other.to_dict()

        new_dict = {}
        for key in self_as_dict:
            new_dict[key] = self._copy_dict_key(key,
                                                original = self_as_dict,
                                                other = other_as_dict,
                                                overwrite = overwrite,
                                                **kwargs)

        cls = other.__class__

        other = cls.from_dict(new_dict)

        return other
