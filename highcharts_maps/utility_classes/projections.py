from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_maps import errors
from highcharts_maps.decorators import class_sensitive, validate_types
from highcharts_maps.metaclasses import HighchartsMeta
from highcharts_maps.utility_classes.javascript_functions import (JavaScriptClass,
                                                                  CallbackFunction)
from highcharts_maps.js_literal_functions import (serialize_to_js_literal,
                                                  assemble_js_literal)


class CustomProjection(JavaScriptClass):
    """The configuration of a custom :term:`projection`, which will be calculated
    client-side using JavaScript.

    Please note that a :class:`CustomProjection` instance *must* include methods with the
    following `function_name`` in its
    :meth:`.methods <highcharts_maps.utility_classes.projections.CustomProjection>`
    property:

      * ``constructor``
      * ``forward`` (with one argument)
      * ``inverse`` (with one argument)

    .. seealso::

      * :ref:`Using Custom Projections <custom_projections>`

    """

    def __init__(self, **kwargs):
        self._name = None

        self.name = kwargs.get('name', None)

        super().__init__(**kwargs)

    def __str__(self) -> str:
        name = self.name or self.class_name

        as_str = super().__str__()
        as_str += ';\n'
        as_str += 'Highcharts.Projection.add('
        as_str += f"'{name}', {self.class_name}"
        as_str += ');'

        return as_str

    @property
    def name(self) -> Optional[str]:
        """The name that is given to the custom :term:`projection`. This is the name that
        you will then reference when applying the projection through a set of
        :class:`ProjectionOptions <highcharts_maps.utility_classes.projections.ProjectionOptions>`.

        If :obj:`None <python:None>`, will default to the custom projection's
        :meth:`.class_name <highcharts_maps.utility_classes.projections.CustomProjection.class_name>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def methods(self) -> Optional[List[CallbackFunction]]:
        """Collection of methods that are to be defined within the class. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          All methods *must* have a :meth:`function_name <CallbackFunction.function_name>`
          set.

        .. warning::

          The list of methods *must* include methods with:

            * a :meth:`function_name <CallbackFunction.function_name>` of
              ``'constructor'`` and be used as a constructor for the class,
            * a :meth:`function_name <CallbackFunction.function_name>` of ``'forward'``
              which accepts a single argument (``lonLat``, by convention)
            * a :meth:`function_name <CallbackFunction.function_name>` of ``'inverse'``
              which accepts a single arugment (``point``, by convention)

        .. note::

          For the sake of simplicity, the :class:`JavaScriptClass` does not support
          ECMAScript's more robust public/private field declaration syntax, nor does it
          support the definition of getters or generators.

        :rtype: :class:`list <python:list>` of :class:`CallbackFunction`, or
          :obj:`None <python:None>`

        :raises HighchartsValueError: if there are fewer than three methods
        :raises HighchartsJavaScriptError: if one or more methods lacks a function name OR
          if any required methods are not included OR if methods do not have the expected
          nmumber of arguments
        """
        return self._methods

    @methods.setter
    def methods(self, value):
        if not value:
            self._methods = None
        else:
            value = validate_types(value,
                                   types = CallbackFunction,
                                   force_iterable = True)
            has_constructor = False
            has_forward = False
            has_inverse = False
            for method in value:
                if not method.function_name:
                    raise errors.HighchartsJavaScriptError('All JavaScriptClass methods '
                                                           'require a function name.')
                if method.function_name == 'constructor':
                    has_constructor = True
                if method.function_name == 'forward':
                    has_forward = True
                    if len(method.arguments) != 1:
                        raise errors.HighchartsJavaScriptError(f'The "forward" method '
                                                               f'expects 1 argument. '
                                                               f'Yours had: '
                                                               f'{len(method.arguments)}')
                if method.function_name == 'inverse':
                    has_inverse = True
                    if len(method.arguments) != 1:
                        raise errors.HighchartsJavaScriptError(f'The "inverse" method '
                                                               f'expects 1 argument. '
                                                               f'Yours had: '
                                                               f'{len(method.arguments)}')

            if len(value) < 3:
                raise errors.HighchartsValueError(f'A CustomProjection requires at least '
                                                  f'three methods, where one is named '
                                                  f'"constructor", one "forward", and '
                                                  f'one "inverse". Received only '
                                                  f'{len(value)} methods.')
            if not has_constructor:
                raise errors.HighchartsJavaScriptError('A JavaScriptClass requires at '
                                                       'least one "constructor" method. '
                                                       'Yours had none.')
            if not has_forward:
                raise errors.HighchartsJavaScriptError('CustomProjection requires a '
                                                       '"forward" method. Yours had '
                                                       'none.')
            if not has_inverse:
                raise errors.HighchartsJavaScriptError('CustomProjection requires a '
                                                       '"inverse" method. Yours had '
                                                       'none.')

            self._methods = value


class ProjectionOptions(HighchartsMeta):
    """The projection options allow applying client-side :term:`projection` to a map given
    in geographic coordinates, typically from :term:`TopoJSON` or :term:`GeoJSON`."""

    def __init__(self, **kwargs):
        self._name = None
        self._parallels = None
        self._rotation = None
        self._custom = None

        self.name = kwargs.get('name', None)
        self.parallels = kwargs.get('parallels', None)
        self.rotation = kwargs.get('rotation', None)
        self.custom = kwargs.get('custom', None)

    @property
    def name(self) -> Optional[str]:
        """The name of the :term:`projection` to apply. Defaults to
        :obj:`None <python:None>`.

        Supports the following built-in values:

          * ``'EqualEarth'``
          * ``'LambertConformalConic'``
          * ``'Miller'``
          * ``'Orthographic'``
          * ``'WebMercator'``

        .. note::

          Will accept any string, including the name given to a custom :term:`projection`
          that has been registered with the chart. For more information, please see:
          :ref:`Using a Custom Projection <custom_projections>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def parallels(self) -> Optional[List[int | float | Decimal]]:
        """In a conic :term:`projection` (e.g. a
        `Lambert Conformal Conic <https://en.wikipedia.org/wiki/Lambert_conformal_conic_projection>`__)
        the two standard parallels that define the map layout. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Expects an iterable with two numerical values. If only one numerical value is
          supplied, the same value will be used for both parallels.

        :rtype: :class:`list <python:list>` of numeric values, or :obj:`None <python:None>`
        """
        return self._parallels

    @parallels.setter
    def parallels(self, value):
        if value is None:
            self._parallels = None
        else:
            if not checkers.is_iterable(value):
                value = [value, value]

            self._parallels = [validators.numeric(x) for x in value]

    @property
    def rotation(self) -> Optional[List[int | float | Decimal]]:
        """The three-axis spherical rotation to apply to the :term:`projection`, expressed
        in degrees. When supplied, the rotation is applied to the globe prior to the
        projection. Defaults to :obj:`None <python:None>`.

        .. note::

          The three-axis spherical rotation expect values for:

            * ``lambda`` - which shifts the the longitudes by the degrees specified,
            * ``phi`` - which (if supplied) shifts the latitudes by the degrees specified,
            * ``gamma`` - which (if supplied) applies a roll to the globe.

          Note that only one value - ``lambda`` - is required. The others can be omitted
          or left as :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of numeric values, or
          :obj:`None <python:None>`
        """
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        if not value:
            self._rotation = None
        else:
            if not checkers.is_iterable(value):
                value = [value]

            processed = [validators.numeric(x, allow_empty = True) for x in value]
            if len(processed) > 3:
                raise errors.HighchartsValueError(f'rotation expects at most three '
                                                  f'member values. Received: '
                                                  f'{len(processed)}.')

    @property
    def custom(self) -> Optional[CustomProjection]:
        """The definition of a custom projection that should be used.

        :rtype: :class:`CustomProjection <highcharts_maps.utility_classes.projections.CustomProjection>`
          or :obj:`None <python:None>`
        """
        return self._custom

    @custom.setter
    @class_sensitive(CustomProjection)
    def custom(self, value):
        self._custom = value
        if value is not None:
            self.name = self.custom.name

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'name': as_dict.get('name', None),
            'parallels': as_dict.get('parallels', None),
            'rotation': as_dict.get('rotation', None),
            'custom': as_dict.get('custom', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'name': self.name,
            'parallels': self.parallels,
            'rotation': self.rotation,
            'custom': self.custom,
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

        untrimmed = self._to_untrimmed_dict()
        if untrimmed.get('custom', None):
            del untrimmed['custom']
        as_dict = {}
        for key in untrimmed:
            item = untrimmed[key]
            serialized = serialize_to_js_literal(item,
                                                 encoding = encoding,
                                                 careful_validation = careful_validation)
            if serialized is not None:
                as_dict[key] = serialized

        as_str = assemble_js_literal(as_dict,
                                     careful_validation = careful_validation)

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str
