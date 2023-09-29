from typing import Optional, List, Dict
from collections import UserDict
from decimal import Decimal

from validator_collection import validators, checkers
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

from highcharts_maps import constants, errors, utility_functions
from highcharts_maps.decorators import class_sensitive, validate_types
from highcharts_maps.options.series.data.base import DataCore
from highcharts_maps.options.series.data.collections import DataPointCollection
from highcharts_maps.utility_classes.data_labels import DataLabel
from highcharts_maps.utility_classes.geojson import Feature


class GeometricDataBase(DataCore):
    """Base class for representing geometric data on map charts."""

    def __init__(self, **kwargs):
        self._data_labels = None
        self._drilldown = None
        self._geometry = None
        self._properties = None

        self.data_labels = kwargs.get('data_labels', None)
        self.drilldown = kwargs.get('drilldown', None)
        self.geometry = kwargs.get('geometry', None)
        self.properties = kwargs.get('properties', None)

        super().__init__(**kwargs)

    @property
    def data_labels(self) -> Optional[DataLabel | List[DataLabel]]:
        """Individual data label for the data point.

        .. note::

          To have multiple data labels per data point, you can also supply a collection of
          :class:`DataLabel` configuration settings.

        :rtype: :class:`DataLabel`, :class:`list <python:list>` of :class:`DataLabel`, or
          :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    def data_labels(self, value):
        if not value:
            self._data_labels = None
        else:
            if checkers.is_iterable(value):
                self._data_labels = validate_types(value,
                                                   types = DataLabel,
                                                   allow_none = False,
                                                   force_iterable = True)
            else:
                self._data_labels = validate_types(value,
                                                   types = DataLabel,
                                                   allow_none = False)

    @property
    def drilldown(self) -> Optional[str]:
        """The :meth:`id <SeriesBase.id>` of a series in the ``drilldown.series`` array
        to use as a drilldown destination for this point. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drilldown

    @drilldown.setter
    def drilldown(self, value):
        self._drilldown = validators.string(value, allow_empty = True)

    @property
    def geometry(self) -> Optional[Feature]:
        """The :term:`geometry <map geometry>` associated with a data point, expressed as
        a :term:`GeoJSON`
        :class:`Feature <highcharts_maps.utility_classes.geojson.Feature>`. Defaults to
        :obj:`None <python:None>`.

        .. tip::

          **Best practice!**

          To make your code easier to maintain through better separation between your
          visualization's structure (e.g. the rendered map) and the data visualized within
          that structure, it is recommended to leave ``.geometry`` empty and to use
          the series'
          :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>`
          property to define the map's geometry.

        :rtype: :class:`Feature <highcharts_maps.utility_classes.geojson.Feature>`
        """
        return self._geometry

    @geometry.setter
    @class_sensitive(Feature)
    def geometry(self, value):
        self._geometry = value

    @property
    def properties(self) -> Optional[dict]:
        """Collection of properties associated with the geometric data point.
        
        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._properties
    
    @properties.setter
    def properties(self, value):
        self._properties = validators.dict(value, allow_empty = True)

    @classmethod
    def from_array(cls, value):
        """Creates a collection of data point instances, parsing the contents of ``value``
        as an array (iterable). This method is specifically used to parse data that is
        input to **Highcharts for Python** without property names, in an array-organized
        structure as described in the `Highcharts JS <https://www.highcharts.com>`__
        documentation.

          .. seealso::

            The specific structure of the expected array is highly dependent on the type
            of data point that the series needs, which itself is dependent on the series
            type itself.

            Please review the detailed :ref:`series documentation <series_documentation>`
            for series type-specific details of relevant array structures.

          .. note::

            An example of how this works for a simple
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` (which
            uses
            :class:`CartesianData <highcharts_core.options.series.data.cartesian.CartesianData>`
            data points) would be:

            .. code-block:: python

              my_series = LineSeries()

              # A simple array of numerical values which correspond to the Y value of the
              # data point
              my_series.data = [0, 5, 3, 5]

              # An array containing 2-member arrays (corresponding to the X and Y values
              # of the data point)
              my_series.data = [
                  [0, 0],
                  [1, 5],
                  [2, 3],
                  [3, 5]
              ]

              # An array of dict with named values
              my_series.data = [
                {
                    'x': 0,
                    'y': 0,
                    'name': 'Point1',
                    'color': '#00FF00'
                },
                {
                    'x': 1,
                    'y': 5,
                    'name': 'Point2',
                    'color': '#CCC'
                },
                {
                    'x': 2,
                    'y': 3,
                    'name': 'Point3',
                    'color': '#999'
                },
                {
                    'x': 3,
                    'y': 5,
                    'name': 'Point4',
                    'color': '#000'
                }
              ]

        :param value: The value that should contain the data which will be converted into
          data point instances.

          .. note::

            If ``value`` is not an iterable, it will be converted into an iterable to be
            further de-serialized correctly.

        :type value: iterable

        :returns: Collection of :term:`data point` instances (descended from
          :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`)
        :rtype: :class:`list <python:list>` of
          :class:`GeometricDataBase <highcharts_maps.options.series.data.geometric.GeometricDataBase>`
          descendant instances or 
          :class:`GeometricDataCollection <highcharts_maps.options.series.data.geometric.GeometricDataCollection>`
        """
        if not utility_functions.is_ndarray(value) and not value:
            return []
        elif utility_functions.is_ndarray(value):
            return cls.from_ndarray(value)

        if checkers.is_type(value, 'DataPointCollection'):
            return value

        return cls.from_list(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'geometry': as_dict.get('geometry', None),
        }

        properties = {}
        if len(as_dict) > len(kwargs):
            for key in as_dict:
                if key not in kwargs:
                    snake_key = utility_functions.to_snake_case(key)
                    if snake_key not in kwargs:
                        properties[snake_key] = as_dict[key]

        kwargs['properties'] = properties

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dataLabels': self.data_labels,
            'drilldown': self.drilldown,
            'geometry': self.geometry,
        }
        if self.properties:
            for key in self.properties:
                untrimmed[key] = self.properties[key]

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class GeometricData(GeometricDataBase):
    """Data point that can be represented on a map visualization."""

    def __init__(self, **kwargs):
        self._middle_x = None
        self._middle_y = None
        self._path = None
        self._value = None

        self.middle_x = kwargs.get('middle_x', None)
        self.middle_y = kwargs.get('middle_y', None)
        self.path = kwargs.get('path', None)
        self.value = kwargs.get('value', None)

        super().__init__(**kwargs)

    @property
    def middle_x(self) -> Optional[int | float | Decimal]:
        """The horizontal mid-point of the map area corresponding to the data point (used
        to place the data label), expressed as a numerical value between ``0`` and ``1``.
        Defaults to ``0.5``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._middle_x

    @middle_x.setter
    def middle_x(self, value):
        self._middle_x = validators.numeric(value,
                                            allow_empty = True,
                                            minimum = 0,
                                            maximum = 1)

    @property
    def middle_y(self) -> Optional[int | float | Decimal]:
        """The vertical mid-point of the map area corresponding to the data point (used
        to place the data label), expressed as a numerical value between ``0`` and ``1``.
        Defaults to ``0.5``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._middle_y

    @middle_y.setter
    def middle_y(self, value):
        self._middle_y = validators.numeric(value,
                                            allow_empty = True,
                                            minimum = 0,
                                            maximum = 1)

    @property
    def path(self) -> Optional[str]:
        """The SVG path of the shape associated with the data point. Defaults to
        :obj:`None <python:None>`.

        .. tip::

          **Best practice!**

          To make your code easier to maintain through better separation between your
          visualization's structure (e.g. the rendered map) and the data visualized within
          that structure, it is recommended to leave ``.geometry`` empty and to use
          the series'
          :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>`
          property to define the map's geometry.

        .. caution::

          For compatibily with old IE, not all SVG path definitions are supported, but M,
          L, and C operators are supported.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._path

    @path.setter
    def path(self, value):
        self._path = validators.string(value, allow_empty = True)

    @property
    def value(self) -> Optional[int | float | Decimal | constants.EnforcedNullType]:
        """The ``value`` of the data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        if value_ is None or isinstance(value_, constants.EnforcedNullType):
            self._value = None
        else:
            self._value = validators.numeric(value_)

    def populate_from_array(self, value):
        """Update the data point's properties with values provided by an array (iterable).
        
        This method is used to parse data that is input to **Highcharts for Python** 
        without property names, in an array-organized
        structure as described in the `Highcharts JS <https://www.highcharts.com>`__
        documentation.
        
          .. seealso::

            The specific structure of the expected array is highly dependent on the type
            of data point that the series needs, which itself is dependent on the series
            type itself.

            Please review the detailed :ref:`series documentation <series_documentation>`
            for series type-specific details of relevant array structures.

          .. note::

            An example of how this works for a simple
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` (which
            uses
            :class:`CartesianData <highcharts_core.options.series.data.cartesian.CartesianData>`
            data points) would be:

            .. code-block:: python

              my_data_point = CartesianData()

              # A simple array of numerical values which correspond to the Y value of the
              # data point
              my_data_point.populate_from_array([0, 0])
              my_data_point.populate_from_array([1, 5])
              my_data_point.populate_from_array([2, 3])
              my_data_point.populate_from_array([3, 5])

        :param value: The value that should contain the data which will be converted into
          data point property values.

          .. note::

            If ``value`` is not an iterable, it will be converted into an iterable to be
            further de-serialized correctly.

        :type value: iterable

        """
        if HAS_NUMPY:
            is_ndarray = isinstance(value, np.ndarray)
        else:
            is_ndarray = False
            
        if not is_ndarray and not checkers.is_iterable(value,
                                                       forbid_literals = (
                                                           str,
                                                           bytes,
                                                           dict,
                                                           UserDict
                                                       )):
            value = [value]

        try:
            properties = self._get_props_from_array(len(value))
        except KeyError:
            full_properties = self._get_props_from_array()
            if len(full_properties) == len(value):
                properties = full_properties
            else:
                properties = []

        if len(value) == 0:
            value = [None for x in properties]

        if len(value) < len(properties):
            value = value[:len(properties)]

        processed_x = False
        processed_name = False
        for index, prop in enumerate(properties):
            if hasattr(value[index], 'item'):
                item = value[index].item()
            else:
                item = value[index]
            setattr(self, prop, item)
            if prop == 'name' and item is not None:
                processed_name = True
            if prop == 'x':
                processed_x = True

        if processed_x and not processed_name and hasattr(self, 'x'):
            if not self.name and checkers.is_string(self.x):
                self.name = self.x
                self.x = None
        
    @classmethod
    def from_array(cls, value):
        """Creates a collection of data point instances, parsing the contents of ``value``
        as an array (iterable). This method is specifically used to parse data that is
        input to **Highcharts for Python** without property names, in an array-organized
        structure as described in the `Highcharts JS <https://www.highcharts.com>`__
        documentation.

          .. seealso::

            The specific structure of the expected array is highly dependent on the type
            of data point that the series needs, which itself is dependent on the series
            type itself.

            Please review the detailed :ref:`series documentation <series_documentation>`
            for series type-specific details of relevant array structures.

          .. note::

            An example of how this works for a simple
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` (which
            uses
            :class:`CartesianData <highcharts_core.options.series.data.cartesian.CartesianData>`
            data points) would be:

            .. code-block:: python

              my_series = LineSeries()

              # A simple array of numerical values which correspond to the Y value of the
              # data point
              my_series.data = [0, 5, 3, 5]

              # An array containing 2-member arrays (corresponding to the X and Y values
              # of the data point)
              my_series.data = [
                  [0, 0],
                  [1, 5],
                  [2, 3],
                  [3, 5]
              ]

              # An array of dict with named values
              my_series.data = [
                {
                    'x': 0,
                    'y': 0,
                    'name': 'Point1',
                    'color': '#00FF00'
                },
                {
                    'x': 1,
                    'y': 5,
                    'name': 'Point2',
                    'color': '#CCC'
                },
                {
                    'x': 2,
                    'y': 3,
                    'name': 'Point3',
                    'color': '#999'
                },
                {
                    'x': 3,
                    'y': 5,
                    'name': 'Point4',
                    'color': '#000'
                }
              ]

        :param value: The value that should contain the data which will be converted into
          data point instances.

          .. note::

            If ``value`` is not an iterable, it will be converted into an iterable to be
            further de-serialized correctly.

        :type value: iterable

        :returns: Collection of :term:`data point` instances (descended from
          :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`)
        :rtype: :class:`list <python:list>` of
          :class:`GeometricDataBase <highcharts_maps.options.series.data.geometric.GeometricDataBase>`
          descendant instances or 
          :class:`GeometricDataCollection <highcharts_maps.options.series.data.geometric.GeometricDataCollection>`
        """
        if not utility_functions.is_ndarray(value) and not value:
            return []
        elif utility_functions.is_ndarray(value):
            return cls.from_ndarray(value)

        if checkers.is_type(value, 'DataPointCollection'):
            return value

        return cls.from_list(value)

    @classmethod
    def from_list(cls, value):
        if not value:
            return []
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'GeometricData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType) or \
                 checkers.is_numeric(item):
                as_obj = cls(value = item)
            elif checkers.is_iterable(item):
                if len(item) != 2:
                    raise errors.HighchartsValueError(f'data expects either a 1D or 2D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')
                as_dict = {
                    'name': item[0],
                    'value': item[1]
                }
                as_obj = cls.from_dict(as_dict)
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Geometric Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return GeometricDataCollection.from_ndarray(value)

    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [2]

    def _get_props_from_array(self, length = None) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_maps.options.series.data.geometric.GeometricData.from_array>`
        method.
        
        :param length: The length of the array, which may determine the properties to 
          parse. Defaults to :obj:`None <python:None>`, which returns the full list of 
          properties.
        :type length: :class:`int <python:int>` or :obj:`None <python:None>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return ['name', 'value']

    @property
    def requires_js_object(self) -> bool:
        """Indicates whether or not the data point *must* be serialized to a JS literal 
        object or whether it can be serialized to a primitive array.
        
        :returns: ``True`` if the data point *must* be serialized to a JS literal object.
          ``False`` if it can be serialized to an array.
        :rtype: :class:`bool <python:bool>`
        """
        from_array_props = [utility_functions.to_camelCase(x)
                            for x in self._get_props_from_array()]
        
        as_dict = self.to_dict()
        trimmed_dict = self.trim_dict(as_dict)
        for prop in from_array_props:
            if prop in trimmed_dict:
                del trimmed_dict[prop]

        if trimmed_dict:
            return True
        
        return False

    def to_array(self, force_object = False) -> List | Dict:
        """Generate the array representation of the data point (the inversion 
        of 
        :meth:`.from_array() <highcharts_maps.options.series.data.geometric.GeometricData.from_array>`).
        
        .. warning::
        
          If the data point *cannot* be serialized to a JavaScript array,
          this method will instead return the untrimmed :class:`dict <python:dict>`
          representation of the data point as a fallback.

        :param force_object: if ``True``, forces the return of the instance's
          untrimmed :class:`dict <python:dict>` representation. Defaults to ``False``.
        :type force_object: :class:`bool <python:bool>`

        :returns: The array representation of the data point.
        :rtype: :class:`list <python:list>` of values or :class:`dict <python:dict>`
        """
        if self.requires_js_object or force_object:
            return self._to_untrimmed_dict()

        return [getattr(self, x, constants.EnforcedNull)
                for x in self._get_props_from_array()]

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'geometry': as_dict.get('geometry', None),

            'middle_x': as_dict.get('middleX', None),
            'middle_y': as_dict.get('middleY', None),
            'path': as_dict.get('path', None),
            'value': as_dict.get('value', None),
        }

        properties = {}
        for key in as_dict:
            if key in kwargs:
                continue
            snake_key = utility_functions.to_snake_case(key)
            if snake_key not in kwargs:
                properties[snake_key] = as_dict[key]
                
        kwargs['properties'] = properties

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'middleX': self.middle_x,
            'middleY': self.middle_y,
            'path': self.path,
            'value': self.value,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class GeometricDataCollection(DataPointCollection):
    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return GeometricData


class GeometricZData(GeometricDataBase):
    """Data point that can be represented on a
    :class:`MapBubbleSeries <highcharts_maps.options.series.mapbubble.MapBubbleSeries>`
    featuring a ``z`` value."""

    def __init__(self, **kwargs):
        self._z = None

        self.z = kwargs.get('z', None)

        super().__init__(**kwargs)

    @property
    def z(self) -> Optional[int | float | Decimal | constants.EnforcedNullType]:
        """The ``value`` of the data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._z

    @z.setter
    def z(self, value):
        if value is None or isinstance(value, constants.EnforcedNullType):
            self._z = None
        else:
            self._z = validators.numeric(value)

    @classmethod
    def from_list(cls, value):
        if not value:
            return []
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'GeometricZData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType) or \
                 checkers.is_numeric(item):
                as_obj = cls(z = item)
            elif checkers.is_iterable(item):
                if len(item) != 1:
                    raise errors.HighchartsValueError(f'data expects a 1D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')
                as_dict = {
                    'z': item[0]
                }
                as_obj = cls.from_dict(as_dict)
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Geometric Z-Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return GeometricZDataCollection.from_ndarray(value)

    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [1]

    def _get_props_from_array(self, length = None) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_maps.options.series.data.geometric.GeometricData.from_array>`
        method.
        
        :param length: The length of the array, which may determine the properties to 
          parse. Defaults to :obj:`None <python:None>`, which returns the full list of 
          properties.
        :type length: :class:`int <python:int>` or :obj:`None <python:None>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return ['z']

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'geometry': as_dict.get('geometry', None),
            'z': as_dict.get('z', None),
        }

        properties = {}
        for key in as_dict:
            if key in kwargs:
                continue
            snake_key = utility_functions.to_snake_case(key)
            if snake_key not in kwargs:
                properties[snake_key] = as_dict[key]
                
        kwargs['properties'] = properties

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'z': self.z
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class GeometricZDataCollection(DataPointCollection):
    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return GeometricZData


class GeometricLatLonData(GeometricDataBase):
    """Data point that can be represented on a
    :class:`MapPointSeries <highcharts_maps.options.series.mappoint.MapPointSeries>`
    featuring latitude/longitude coordinates, an x-value, and a y-value."""

    def __init__(self, **kwargs):
        self._lat = None
        self._lon = None
        self._x = None
        self._y = None

        self.lat = kwargs.get('lat', None)
        self.lon = kwargs.get('lon', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

        super().__init__(**kwargs)

    @property
    def lat(self) -> Optional[int | float | Decimal]:
        """The latitude of the data point. Defaults to :obj:`None <python:None>`.

        .. warning::

          Must be combined with the
          :meth:`.lon <highcharts_maps.options.series.data.geometric.GeometricLatLonData.lon>`
          to work as expected.

        ..warning::

          Overrides the
          :meth:`.x <highcharts_maps.options.series.data.geometric.GeometricLatLonData.x>`
          value if set.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = validators.numeric(value, allow_empty = True)

    @property
    def lon(self) -> Optional[int | float | Decimal]:
        """The longitude of the data point. Defaults to :obj:`None <python:None>`.

        .. warning::

          Must be combined with the
          :meth:`.lat <highcharts_maps.options.series.data.geometric.GeometricLatLonData.lat>`
          to work as expected.

        .. warning::

          Overrides the
          :meth:`.y <highcharts_maps.options.series.data.geometric.GeometricLatLonData.y>`
          value if set.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = validators.numeric(value, allow_empty = True)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The x-coordinate of the data point, expressed in projected units. Defaults to
        :obj:`None <python:None>`.

        :rytpe: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal | constants.EnforcedNullType]:
        """The y-coordinate of the data point, expressed in projected units. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        if value is None or isinstance(value, constants.EnforcedNullType):
            self._y = None
        else:
            self._y = validators.numeric(value)

    @classmethod
    def from_list(cls, value):
        if not value:
            return []
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'GeometricLatLonData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType) or \
                 checkers.is_numeric(item):
                as_obj = cls(y = item)
            elif checkers.is_iterable(item):
                if len(item) != 2:
                    raise errors.HighchartsValueError(f'data expects either a 1D or 2D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')
                as_dict = {
                    'name': item[0],
                    'y': item[1]
                }
                as_obj = cls.from_dict(as_dict)
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Geometric Lat/Lon Data Point or '
                                                  f'be coercable to one. Could not coerce:'
                                                  f' {item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return GeometricLatLonDataCollection.from_ndarray(value)

    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [2]

    def _get_props_from_array(self, length = None) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_maps.options.series.data.geometric.GeometricLatLonData.from_array>`
        method.
        
        :param length: The length of the array, which may determine the properties to 
          parse. Defaults to :obj:`None <python:None>`, which returns the full list of 
          properties.
        :type length: :class:`int <python:int>` or :obj:`None <python:None>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return ['name', 'y']

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'geometry': as_dict.get('geometry', None),
            'lat': as_dict.get('lat', None),
            'lon': as_dict.get('lon', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        properties = {}
        if len(as_dict) > len(kwargs):
            for key in as_dict:
                if key not in kwargs:
                    snake_key = utility_functions.to_snake_case(key)
                    if snake_key not in kwargs:
                        properties[snake_key] = as_dict[key]
                
        kwargs['properties'] = properties

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'lat': self.lat,
            'lon': self.lon,
            'x': self.x,
            'y': self.y,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class GeometricLatLonDataCollection(DataPointCollection):
    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return GeometricLatLonData
