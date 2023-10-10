from typing import Optional
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

import esprima
from esprima.error_handler import Error as ParseError

from validator_collection import validators, checkers

from highcharts_maps import errors, utility_functions
from highcharts_maps.decorators import validate_types
from highcharts_maps.metaclasses import HighchartsMeta
from highcharts_maps.utility_classes.topojson import Topology


class GeoJSONBase(HighchartsMeta):
    """Base class used to implement standard methods that can be mixed-in to the
    Highcharts maps for Python GeoJSON implementation."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        as_json = self.to_json()
        as_dict = json.loads(as_json)

        return as_dict

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {}

        return kwargs

    @classmethod
    def from_json(cls,
                  as_json_or_file: str | bytes,
                  allow_snake_case: bool = True):
        """Construct an instance of the class from a JSON string.

        :param as_json_or_file: The JSON string for the object or the filename of a file
          that contains the JSON string.
        :type as_json: :class:`str <python:str>` or :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_json``.
        :rtype: :class:`HighchartsMeta`
        """
        is_file = checkers.is_file(as_json_or_file)
        if is_file:
            with open(as_json_or_file, 'r') as file_:
                as_str = file_.read()
        else:
            as_str = as_json_or_file

        return geojson.loads(as_str)

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

        try:
            as_json = geojson.dumps(self, encoding = encoding)
        except TypeError:
            as_json = geojson.dumps(self)

        if filename:
            if isinstance(as_json, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_json)

        return as_json

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
        return self.to_json(filename = filename,
                            encoding = encoding)

    @classmethod
    def _validate_js_literal(cls,
                             as_str,
                             range = True,
                             _break_loop_on_failure = False):
        """Parse ``as_str`` as a valid JavaScript literal object.

        :param as_str: The string to parse as a JavaScript literal object.
        :type as_str: :class:`str <python:str>`

        :param range: If ``True``, includes location and range data for each node in the
          AST returned. Defaults to ``False``.
        :type range: :class:`bool <python:bool>`

        :param _break_loop_on_failure: If ``True``, will not loop if the method fails to
          parse/validate ``as_str``. Defaults to ``False``.
        :type _break_loop_on_failure: :class:`bool <python:bool>`

        :returns: The parsed AST representation of ``as_str`` and the updated string.
        :rtype: 2-member :class:`tuple <python:tuple>` of :class:`esprima.nodes.Script`
          and :class:`str <python:str>`
        """
        if """document.addEventListener('DOMContentLoaded', function() {\n""" in as_str:
            as_str = as_str.replace(
                """document.addEventListener('DOMContentLoaded', function() {\n""", ''
            )
            as_str = as_str[:-3]
        try:
            parsed = esprima.parseScript(as_str, loc = range, range = range)
        except ParseError:
            try:
                parsed = esprima.parseModule(as_str, loc = range, range = range)
            except ParseError:
                if not _break_loop_on_failure:
                    as_str = f"""var randomVariable = {as_str}"""
                    return cls._validate_js_literal(as_str,
                                                    range = range,
                                                    _break_loop_on_failure = True)
                else:
                    raise errors.HighchartsParseError('._validate_js_literal() expects '
                                                      'a str containing a valid '
                                                      'JavaScript literal object. Could '
                                                      'not find a valid literal.')

        return parsed, as_str

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
        :type other: :class:`GeoJSONBase`

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
        return cls(**as_dict)

    def to_dict(self) -> dict:
        """Generate a :class:`dict <python:dict>` representation of the object compatible
        with the Highcharts JavaScript library.

        .. note::

          The :class:`dict <python:dict>` representation has a property structure and
          naming convention that is *intentionally* consistent with the Highcharts
          JavaScript library. This is not Pythonic, but it makes managing the interplay
          between the two languages much, much simpler.

        :returns: A :class:`dict <python:dict>` representation of the object.
        :rtype: :class:`dict <python:dict>`
        """
        untrimmed = self._to_untrimmed_dict()

        return untrimmed

    def to_topojson(self) -> Topology:
        """Convert the object into a :term:`TopoJSON`
        :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>` object.

        :rtype: :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>`
        """
        as_json = self.to_json()

        return Topology.from_geojson(as_json)

    @classmethod
    def from_topojson(cls, as_topojson):
        """Convert a :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>`
        instance into a
        :class:`GeoJSONBase <highcharts_maps.utility_classes.geojson.GeoJSONBase>`
        instance.

        :param as_topojson: The :term:`TopoJSON` object or collection to convert.
        :type as_topojson: :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>`

        :rtype: :class:`GeoJSONBase <highcharts_maps.utility_classes.geojson.GeoJSONBase>`
        """
        if not isinstance(as_topojson, Topology):
            as_topojson = validate_types(as_topojson, Topology)

        as_geojson = as_topojson.to_geojson()

        return cls.from_json(as_geojson)

    @classmethod
    def to_instance(cls, ob, default = None, strict = False):
        """Encode a GeoJSON :class:`dict <python:dict>` into an :class:`GeoJSONBase`
        object.

        .. note::

          Assumes the caller knows that the :class:`dict <python:dict>` should satisfy a
          GeoJSON type.

        :param cls: :class:`dict <python:dict>` containing the elements to be encoded into
          a GeoJSON object.
        :type cls: :class:`dict <python:dict>`

        :param ob: GeoJSON object into which to encode the :class:`dict <python:dict>`
          provided in ``cls``.

        :type ob: :class:`geojson.base.GeoJSON <geojson:geojson.base.GeoJSON>`

        :param default: A default instance to append the content of the
          :class:`dict <python:dict>`. Defaults to :obj:`None <python:None>`.
        :type default: :class:`geojson.base.GeoJSON <geojson:geojson.base.GeoJSON>`

        :param strict: Raise error if unable to coerce particular keys or
          attributes to a valid GeoJSON structure. Defaults to ``False``.
        :type strict: :class:`bool <python:bool>`

        :return: A GeoJSON object with the dict's elements as its constituents.
        :rtype: :class:`geojson.base.GeoJSON <geojson:geojson.base.GeoJSON>`

        :raises TypeError: If the input :class:`dict <python:dict>` contains items that
          are not valid GeoJSON types.
        :raises UnicodeEncodeError: If the input :class:`dict <python:dict>` contains
          items of a type that contain non-ASCII characters.
        :raises AttributeError: If the input :class:`dict <python:dict>` contains items
          that are not valid GeoJSON types.
        """
        return super().to_instance(cls = cls,
                                   ob = ob,
                                   default = default,
                                   strict = strict)


class Point(GeoJSONBase, geojson.Point):
    """Represents a GeoJSON ``Point`` as a Python object, inheriting from
    :class:`geojson.Point <geojson:geometry.Point>` with additional
    methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MultiPoint(GeoJSONBase, geojson.MultiPoint):
    """Represents a GeoJSON ``MultiPoint`` as a Python object, inheriting from
    :class:`geojson.MultiPoint <geojson:geometry.MultiPoint>` with additional
    methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LineString(GeoJSONBase, geojson.LineString):
    """Represents a GeoJSON ``LineString`` as a Python object, inheriting from
    :class:`geojson.LineString <geojson:geometry.LineString>` with additional
    methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MultiLineString(GeoJSONBase, geojson.MultiLineString):
    """Represents a GeoJSON ``MultiLineString`` as a Python object, inheriting from
    :class:`geojson.MultiLineString <geojson:geometry.MultiLineString>` with additional
    methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Polygon(GeoJSONBase, geojson.Polygon):
    """Represents a GeoJSON ``Polygon`` as a Python object, inheriting from
    :class:`geojson.Polygon <geojson:geometry.Polygon>` with additional
    methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MultiPolygon(GeoJSONBase, geojson.MultiPolygon):
    """Represents a GeoJSON ``MultiPolygon`` as a Python object, inheriting from
    :class:`geojson.MultiPolygon <geojson:geometry.MultiPolygon>` with additional
    methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GeometryCollection(GeoJSONBase, geojson.GeometryCollection):
    """Represents a GeoJSON ``GeometryCollection`` as a Python object, inheriting from
    :class:`geojson.GeometryCollection <geojson:geometry.GeometryCollection>` with
    additional methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Feature(GeoJSONBase, geojson.Feature):
    """Represents a GeoJSON ``Feature`` as a Python object, inheriting from
    :class:`geojson.Feature <geojson:geometry.Feature>` with additional
    methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FeatureCollection(GeoJSONBase, geojson.FeatureCollection):
    """Represents a GeoJSON ``FeatureCollection`` as a Python object, inheriting from
    :class:`geojson.FeatureCollection <geojson:geometry.FeatureCollection>` with
    additional methods to conform to the
    :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` standard
    interface."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
