from decimal import Decimal
from typing import Optional, List, Any
from collections import UserDict

from validator_collection import validators, checkers

from highcharts_core.options.series.data.connections import *

from highcharts_maps import constants, errors
from highcharts_core.options.series.data.collections import DataPointCollection
from highcharts_maps.decorators import class_sensitive
from highcharts_maps.utility_classes.gradients import Gradient
from highcharts_maps.utility_classes.patterns import Pattern
from highcharts_maps.utility_classes.markers import FlowmapMarker


class FlowmapData(WeightedConnectionData):
    """Variant of :class:`ConnectionData` that also applies a ``weight`` to the
    connection."""
    
    def __init__(self, **kwargs):
        self._curve_factor = None
        self._fill_color = None
        self._fill_opacity = None
        self._grow_towards = None
        self._line_width = None
        self._marker_end = None
        self._opacity = None
        self._weight = None
        
        self.curve_factor = kwargs.get('curve_factor', None)
        self.fill_color = kwargs.get('fill_color', None)
        self.fill_opacity = kwargs.get('fill_opacity', None)
        self.grow_towards = kwargs.get('grow_towards', None)
        self.line_width = kwargs.get('line_width', None)
        self.marker_end = kwargs.get('marker_end', None)
        self.opacity = kwargs.get('opacity', None)
        self.weight = kwargs.get('weight', None)
        
        super().__init__(**kwargs)
        
    @property
    def curve_factor(self) -> Optional[int | float | Decimal]:
        """The amount by which to curve the lines on a flowmap. Higher numbers makes the links 
        more curved, while a value of ``0`` makes the lines straight. Defaults to 
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._curve_factor

    @curve_factor.setter
    def curve_factor(self, value):
        self._curve_factor = validators.numeric(value, allow_empty = True)

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern | constants.EnforcedNullType]:
        """Fill color or gradient for the area. When :class:`EnforcedNullType`, the
        series' color is used with the series'
        :meth:`.fill_opacity <FlowmapOptions.fill_opacity>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`EnforcedNullType`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        from highcharts_maps.utility_functions import validate_color
        self._fill_color = validate_color(value)

    @property
    def fill_opacity(self) -> Optional[int | float | Decimal]:
        """Fill opacity for the area. Defaults to ``0.5``.

        When you set an explicit :meth:`fill_color <FlowmapOptions.fill_color>`, the
        ``fill_opacity`` is not applied. Instead, you should define the opacity in the
        :meth:`fill_color <FlowmapOptions.fill_color>` with an rgba color definition.

        The ``fill_opacity`` setting, also the default setting, overrides the alpha
        component of the color setting.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._fill_opacity

    @fill_opacity.setter
    def fill_opacity(self, value):
        self._fill_opacity = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @staticmethod
    def _validate_coordinates(value) -> Optional[List[int | float | Decimal]]:
        """Processes ``value`` to confirm that they contain valid coordinates, expressed as a ``longitude, latitude``.
        
        :param value: The value to validate.
        :type value: any
        
        :returns: A 2-member :class:`list <python:list>` of the form ``[longitude, latitude]``, or 
          :obj:`None <python:None>`
        :rtype: :class:`list <python:list>` of numeric, or :obj:`None <python:None>`
        """
        if value is None:
            return None
        elif checkers.is_string(value):
            return value
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict, UserDict)):
            if len(value) != 2:
                raise errors.HighchartsValueError(f'.from expects coordinates expressed in longitude, latitude. '
                                                  f'Received a set of coordinates with {len(value)} members.')
            return [validators.numeric(x, allow_empty = False) for x in value]
        elif isinstance(value, (dict, UserDict)):
            missing_keys = []
            reformed_value = []

            if 'lon' in value:
                reformed_value.append(value.get('lon', None))
            elif 'longitude' in value:
                reformed_value = reformed_value.append(value.get('longitude', None))
            else:
                missing_keys.append('longitude')
            
            if 'lat' in value:
                reformed_value.append(value.get('lat', None))
            elif 'latitude' in value:
                reformed_value.append(value.get('latitude', None))
            else:
                missing_keys.append('latitude')

            if missing_keys:
                raise errors.HighchartsValueError(f'.from expects coordinates with both a longitude and a latitude. '
                                                  f'Value received was missing: {missing_keys}')

            return [validators.numeric(x, allow_empty = False) for x in reformed_value]
        else:
            missing_keys = []
            reformed_value = []

            if hasattr(value, 'lon'):
                reformed_value.append(getattr(value, 'lon', None))
            elif hasattr(value, 'longitude'):
                reformed_value.append(getattr(value, 'longitude', None))
            else:
                missing_keys.append('longitude')
            
            if hasattr(value, 'lat'):
                reformed_value.append(getattr(value, 'lat', None))
            elif hasattr(value, 'latitude'):
                reformed_value.append(getattr(value, 'latitude', None))
            else:
                missing_keys.append('latitude')

            if missing_keys:
                raise errors.HighchartsValueError(f'value is expected to a set of coordinates, expressed either '
                                                  f'as an ID (string), a 2-member iterable of numerical coordinates '
                                                  f'of the form [longitude, latitude], a dict with keys '
                                                  f'"longitude"/"lon"  and "latitude"/"lat", or an object with '
                                                  f'properties "longitude"/"lon" and "latitude"/"lat". Value received' 
                                                  f' did not match any of these, and was missing keys/properties: '
                                                  f'{missing_keys}')

            return [validators.numeric(x, allow_empty = False) for x in reformed_value]

    @property
    def from_(self) -> Optional[str | List[int | float | Decimal]]:
        """The coordinates for the link's origin point. Accepts either:

          * an ID referencing a map point holding coordinates of the link origin
          * coordinates expressed as a 2-member array of the form ``[longitude, latitude]``, 
          * :class:`dict <python:dict>` with keys ``'lon'/'longitude'`` and ``'lat'/'latitude'``, or
          * arbitrary object with ``'lon'/'longitude'`` and ``'lat'/'latitude'`` properties.
        
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or iterable of coordinates or :obj:`None <python:None>`
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        self._from_ = self._validate_coordinates(value)
        
    @property
    def to(self) -> Optional[str | List[int | float | Decimal]]:
        """The coordinates for the link's destination. Accepts either:

          * an ID referencing a map point holding coordinates of the link origin
          * coordinates expressed as a 2-member array of the form ``[longitude, latitude]``, 
          * :class:`dict <python:dict>` with keys ``'lon'/'longitude'`` and ``'lat'/'latitude'``, or
          * arbitrary object with ``'lon'/'longitude'`` and ``'lat'/'latitude'`` properties.
        
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or iterable of coordinates or :obj:`None <python:None>`
        """
        return self._to
    
    @to.setter
    def to(self, value):
        self._to = self._validate_coordinates(value)

    @property
    def grow_towards(self) -> Optional[bool]:
        """If ``True``, the line will grow as it approaches its destination. Defaults to :obj:`None <python:None>`.
        
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._grow_towards
    
    @grow_towards.setter
    def grow_towards(self, value):
        if value is None:
            self._grow_towards = None
        else:
            self._grow_towards = bool(value)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the graph line. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def marker_end(self) -> Optional[FlowmapMarker]:
        """If enabled, creates an arrow symbol indicating the direction of the flow at the flow's destination.
        
        .. warning::
        
          Setting/enabling this property in the 
          :class:`FlowmapOptions <highcharts_maps.options.plot_options.flowmap.FlowmapOptions>` object rather than in 
          the :class:`FlowmapSeries <highcharts_maps.options.series.flowmap.FlowmapSeries>` will apply a marker to the 
          end of *every* flowmap series in your visualization.
          
        :rtype: :class:`FlowmapMarker <highcharts_maps.utility_classes.markers.FlowmapMarker>` or 
          :obj:`None <python:None>
        """
        return self._marker_end
    
    @marker_end.setter
    @class_sensitive(FlowmapMarker)
    def marker_end(self, value):
        self._marker_end = value

    @property
    def opacity(self) -> Optional[int | float | Decimal]:
        """Opacity for the link. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = validators.numeric(value,
                                           allow_empty = True,
                                           minimum = 0)

    @property
    def weight(self) -> Optional[int | float | Decimal]:
        """The weight for the link, which determines its thickness compared to other links. Defaults to 
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_list(cls, value):
        """Generator method which produces a collection of :class:`FlowmapData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`FlowmapData` instances
        """
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
            if checkers.is_type(item, 'FlowmapData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            if checkers.is_iterable(item, forbid_literals = (str, bytes, dict, UserDict)):
                if len(item) == 3:
                    as_obj = cls(from_ = item[0],
                                 to = item[1],
                                 weight = item[2])
                else:
                    raise errors.HighchartsValueError(f'FlowmapData expects an array of FlowmapData objects, '
                                                      f'or an iterable coercable to a FlowmapData object. '
                                                      f'However the iterable received could not be coerced.'
                                                      f'Expected a 3-member iterable, but the received iterable '
                                                      f'had {len(item)} members.')
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Connection Data Point or be '
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
        return FlowmapDataCollection.from_ndarray(value)
    
    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [3]

    @classmethod
    def _get_props_from_array(cls, length = None) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`
        method.
        
        :param length: The length of the array, which may determine the properties to 
          parse. Defaults to :obj:`None <python:None>`, which returns the full list of 
          properties.
        :type length: :class:`int <python:int>` or :obj:`None <python:None>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        prop_list = {
            None: ['from_', 'to', 'weight'],
            3: ['from_', 'to', 'weight'],
        }
        return cls._get_props_from_array_helper(prop_list, length)

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
            'label_rank': as_dict.get('labelrank',
                                      None) or as_dict.get('labelRank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'from_': as_dict.get('from', None),
            'to': as_dict.get('to', None),

            'weight': as_dict.get('weight', None),

            'curve_factor': as_dict.get('curveFactor', None),
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'grow_towards': as_dict.get('growTowards', None),
            'line_width': as_dict.get('lineWidth', None),
            'marker_end': as_dict.get('markerEnd', None),
            'opacity': as_dict.get('opacity', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'weight': self.weight,

            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,

            'from': self.from_,
            'to': self.to,

            'accessibility': self.accessibility,
            'className': self.class_name,
            'color': self.color,
            'colorIndex': self.color_index,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'id': self.id,
            'labelrank': self.label_rank,
            'name': self.name,
            'selected': self.selected,

            'curve_factor': self.curve_factor,
            'fill_color': self.fill_color,
            'fill_opacity': self.fill_opacity,
            'grow_towards': self.grow_towards,
            'line_width': self.line_width,
            'marker_end': self.marker_end,
            'opacity': self.opacity,
        }

        return untrimmed


class FlowmapDataCollection(DataPointCollection):
    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return FlowmapData
