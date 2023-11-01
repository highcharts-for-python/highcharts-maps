from decimal import Decimal
from typing import Optional, List

from validator_collection import validators

from highcharts_maps import constants
from highcharts_maps.metaclasses import HighchartsMeta
from highcharts_maps.decorators import class_sensitive, validate_types
from highcharts_maps.options.plot_options.generic import GenericTypeOptions
from highcharts_maps.utility_classes.gradients import Gradient
from highcharts_maps.utility_classes.patterns import Pattern
from highcharts_maps.utility_classes.markers import FlowmapMarker
from highcharts_maps.options.plot_options.map import MapOptions


class InterpolationOptions(HighchartsMeta):
    """Options to configure map interpolation."""
    
    def __init__(self, **kwargs):
        self._blur = None
        self._enabled = None
        
        self.blur = kwargs.get('blur', None)
        self.enabled = kwargs.get('enabled', None)
        
    @property
    def blur(self) -> Optional[int | float | Decimal]:
        """Represents how much blur should be added to the interpolated
        image. Defaults to ``1``.
        
        .. tip::
        
          Works best in the range of ``0 - 1``, all higher values would need 
          higher perfomance to calculate more detailed interpolation.
          
        .. note::
        
          This is useful, if the data is spread into wide range of\n longitue and 
          latitude values.
          
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._blur
    
    @blur.setter
    def blur(self, value):
        self._blur = validators.numeric(value, allow_empty = True)
        
    @property
    def enabled(self) -> Optional[bool]:
        """Enables or disables interpolation. Defaults to ``False``.
        
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'blur': as_dict.get('blur', None),
            'enabled': as_dict.get('enabled', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'blur': self.blur,
            'enabled': self.enabled,
        }

        return untrimmed


class FlowmapOptions(GenericTypeOptions):
    """A :term:`flowmap` series is a series laid out on top of a map series that displays route paths (e.g. flight 
    or naval routes), or directional flows on a map. It creates a link between two points on a map chart.
    
    .. figure:: ../../../_static/flowmap-example.png
      :alt: Flowmap Example chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._animation_limit = None
        self._color_axis = None
        self._color_by_point = None
        self._color_index = None
        self._color_key = None
        self._colors = None
        self._curve_factor = None
        self._fill_color = None
        self._fill_opacity = None
        self._find_nearest_point_by = None
        self._line_width = None
        self._marker_end = None
        self._max_width = None
        self._min_width = None
        self._null_color = None
        self._null_interaction = None
        self._weight = None
        self._width = None
        self._z_index = None
        
        self.animation_limit = kwargs.get('animation_limit', None)
        self.color_axis = kwargs.get('color_axis', None)
        self.color_by_point = kwargs.get('color_by_point', None)
        self.color_index = kwargs.get('color_index', None)
        self.color_key = kwargs.get('color_key', None)
        self.colors = kwargs.get('colors', None)
        self.curve_factor = kwargs.get('curve_factor', None)
        self.fill_color = kwargs.get('fill_color', None)
        self.fill_opacity = kwargs.get('fill_opacity', None)
        self.find_nearest_point_by = kwargs.get('find_nearest_point_by', None)
        self.line_width = kwargs.get('line_width', None)
        self.marker_end = kwargs.get('marker_end', None)
        self.max_width = kwargs.get('max_width', None)
        self.min_width = kwargs.get('min_width', None)
        self.null_color = kwargs.get('null_color', None)
        self.null_interaction = kwargs.get('null_interaction', None)
        self.weight = kwargs.get('weight', None)
        self.width = kwargs.get('width', None)
        self.z_index = kwargs.get('z_index', None)
        
        super().__init__(**kwargs)
        
    @property
    def animation_limit(self) -> Optional[int | float | Decimal]:
        """For some series, there is a limit that shuts down initial animation by default
        when the total number of points in the chart is too high. Defaults to
        :obj:`None <python:None>`.

        For example, for a column chart and its derivatives, animation does not run if
        there is more than 250 points totally. To disable this cap, set
        ``animation_limit`` to ``float("inf")`` (which represents infinity).

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._animation_limit

    @animation_limit.setter
    def animation_limit(self, value):
        if value == float('inf'):
            self._animation_limit = float('inf')
        else:
            self._animation_limit = validators.numeric(value,
                                                       allow_empty = True,
                                                       minimum = 0)

    @property
    def color_axis(self) -> Optional[str | int | bool]:
        """When using dual or multiple color axes, this setting defines which
        :term:`color axis` the particular series is connected to. It refers to either the
        :meth:`ColorAxis.id` or the index of the axis in the :class:`ColorAxis` array,
        with ``0`` being the first. Set this option to ``False`` to prevent a series from
        connecting to the default color axis.

        Defaults to ``0``.

        :rtype: :obj:`None <python:None>` or :class:`str <python:str>` or
          :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._color_axis

    @color_axis.setter
    def color_axis(self, value):
        if value is None:
            self._color_axis = None
        elif value is False:
            self._color_axis = False
        else:
            try:
                self._color_axis = validators.string(value)
            except TypeError:
                self._color_axis = validators.integer(value,
                                                      minimum = 0)

    @property
    def color_by_point(self) -> Optional[bool]:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        if value is None:
            self._color_by_point = None
        else:
            self._color_by_point = bool(value)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def color_key(self) -> Optional[str]:
        """Determines what data value should be used to calculate point color if
        :meth:`FlowmapOptions.color_axis` is used.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color_key

    @color_key.setter
    def color_key(self, value):
        self._color_key = validators.string(value, allow_empty = True)

    @property
    def colors(self) -> Optional[List[str | Gradient | Pattern]]:
        """A series-specific or series type-specific color set to apply instead of the
        global colors when :meth:`FlowmapOptions.color_by_point` is ``True``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`,
          :class:`Gradient`, or :class:`Pattern` OR :obj:`None <python:None>`
        """
        return self._colors

    @colors.setter
    def colors(self, value):
        from highcharts_maps.utility_functions import validate_color
        if not value:
            self._colors = None
        else:
            value = validators.iterable(value)

            self._colors = [validate_color(x) for x in value]

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

    @property
    def find_nearest_point_by(self) -> Optional[str]:
        """Determines whether the series should look for the nearest point in both
        dimensions or just the x-dimension when hovering the series.

        If :obj:`None <python:None>`, defaults to ``'xy'`` for scatter series and ``'x'``
        for most other series. If the data has duplicate x-values, it is recommended to
        set this to ``'xy'`` to allow hovering over all points.

        Applies only to series types using nearest neighbor search (not direct hover) for
        tooltip.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._find_nearest_point_by

    @find_nearest_point_by.setter
    def find_nearest_point_by(self, value):
        self._find_nearest_point_by = validators.string(value, allow_empty = True)

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
    def max_width(self) -> Optional[int | float | Decimal]:
        """The maximum width of a link expressed in pixels. Defaults to ``25``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_width

    @max_width.setter
    def max_width(self, value):
        if value is None:
            self._max_width = None
        else:
            self._max_width = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def min_width(self) -> Optional[int | float | Decimal]:
        """The minimum width of a link expressed in pixels. Defaults to ``5``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_width

    @min_width.setter
    def min_width(self, value):
        if value is None:
            self._min_width = None
        else:
            self._min_width = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def null_color(self) -> Optional[str | Gradient | Pattern]:
        """The color applied to null points. Defaults to ``'#f7f7f7'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._null_color

    @null_color.setter
    def null_color(self, value):
        from highcharts_maps import utility_functions
        self._null_color = utility_functions.validate_color(value)

    @property
    def null_interaction(self) -> Optional[bool]:
        """If ``True``, allows pointer interactions (e.g. tooltips, mouse events, etc.) on null points.
        Defaults to :obj:`None <python:None>`.
        
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._null_interaction
    
    @null_interaction.setter
    def null_interaction(self, value):
        if value is None:
            self._null_interaction = None
        else:
            self._null_interaction = bool(value)

    @property
    def weight(self) -> Optional[int | float | Decimal]:
        """he weight for all links with unspecified weights. The weight of a link determines its thickness compared to 
        other links. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = validators.numeric(value, allow_empty = True)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """If no :meth:`.weight <highcharts_maps.options.plot_options.flowmap.FlowmapOptions.weight>` has previously 
        been specified, this will set the width of all the links without being compared to and scaled according to 
        other weights. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @property
    def z_index(self) -> Optional[int]:
        """The Z-Index for the series. Defaults to :obj:`None <python:None>`.

        :returns: The z-index for the series.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.integer(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),
            
            'animation_limit': as_dict.get('animationLimit', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'colors': as_dict.get('colors', None),
            'curve_factor': as_dict.get('curveFactor', None),
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'line_width': as_dict.get('lineWidth', None),
            'marker_end': as_dict.get('markerEnd', None),
            'max_width': as_dict.get('maxWidth', None),
            'min_width': as_dict.get('minWidth', None),
            'null_color': as_dict.get('nullColor', None),
            'null_interaction': as_dict.get('nullInteraction', None),
            'weight': as_dict.get('weight', None),
            'width': as_dict.get('width', None),
            'z_index': as_dict.get('zIndex', None),

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        from highcharts_maps.utility_functions import mro__to_untrimmed_dict
        
        untrimmed = {
            'animationLimit': self.animation_limit,
            'colorAxis': self.color_axis,
            'colorByPoint': self.color_by_point,
            'colorIndex': self.color_index,
            'colorKey': self.color_key,
            'colors': self.colors,
            'curveFactor': self.curve_factor,
            'fillColor': self.fill_color,
            'fillOpacity': self.fill_opacity,
            'findNearestPointBy': self.find_nearest_point_by,
            'lineWidth': self.line_width,
            'markerEnd': self.marker_end,
            'maxWidth': self.max_width,
            'minWidth': self.min_width,
            'nullColor': self.null_color,
            'nullInteraction': self.null_interaction,
            'weight': self.weight,
            'width': self.width,
            'zIndex': self.z_index,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class GeoHeatmapOptions(MapOptions, FlowmapOptions):
    """A :term:`geoheatmap` series is a variety of heatmap series, composed into the map projection, where the
    units are expressed in latitude and longitude, while individual values contained in a matrix are represented 
    as colors.
    
    .. warning::

      GeoHeatmaps require that ``modules/geoheatmap`` is loaded client-side.

    .. figure:: ../../../_static/geoheatmap-example.png
      :alt: GeoHeatmap Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._colsize = None
        self._interpolation = None
        self._rowsize = None
        
        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.colsize = kwargs.get('colsize', None)
        self.interpolation = kwargs.get('interpolation', None)
        self.rowsize = kwargs.get('rowsize', None)

        super().__init__(**kwargs)
        
    @property
    def all_areas(self) -> Optional[bool]:
        """If ``True``, all areas defined in the map's
        :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>`
        should be rendered, with areas that do not have a related data point rendered as
        null values. If ``False``, areas of the map that do not have a related data point
        are skipped and not rendered. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._all_areas

    @all_areas.setter
    def all_areas(self, value):
        self._all_areas = None

    @property
    def colsize(self) -> Optional[int]:
        """The column size - how many X axis units each column in the heatmap should span.
        Defaults to ``1``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._colsize

    @colsize.setter
    def colsize(self, value):
        self._colsize = validators.integer(value,
                                           allow_empty = True,
                                           minimum = 1)

    @property
    def interpolation(self) -> Optional[bool | InterpolationOptions]:
        """If enabled, render data points as an interpolated image. It can be used to 
        show temperature map-like charts. Defaults to ``False``.
        
        :rtype: :class:`bool <python:bool>` or 
          :class:`InterpolationOptions <highcharts_maps.options.plot_options.flowmap.InterpolationOptions>`
          or :obj:`None <python:None>`
        """
        return self._interpolation
    
    @interpolation.setter
    def interpolation(self, value):
        if value is None:
            self._interpolation = None
        elif isinstance(value, bool):
            self._interpolation = value
        else:
            self._interpolation = validate_types(value, InterpolationOptions)

    @property
    def join_by(self) -> Optional[str | List[str] | constants.EnforcedNullType]:
        """The property which should be used to join the series'
        :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>` to
        its ``.data``. When :obj:`None <python:None>`, defaults to ``'hc-key'``.

        Accepts three possible types of value:

          * a string, which joins on the same property in both the ``.mapData`` and
            ``.data``

            .. note::

              For maps loaded from :term:`GeoJSON`, the keys may be held in each point's
              ``properties`` object.

          * a 2-member collection, where the first represents the key in ``.mapData`` and
            the second represents a (different) key in ``.data``
          * :obj:`highcharts_maps.constants.EnforcedNull`, where items are joined by their
            positions in the ``.mapData`` and ``.data`` arrays

        .. tip::

          Using :obj:`highcharts_maps.constants.EnforcedNull` performs much faster than
          the other two options. This is the recommended value when rendering more than a
          thousand data points, assuming that you are using a backend that can preprocess
          the data into parallel arrays.

        :rtype: :obj:`highcharts_maps.constants.EnforcedNull` or :class:`str <python:str>`
          or 2-member :class:`list <python:list>` of :class:`str <python:list>`, or
          :obj:`None <python:None>`

        :raises HighchartsValueError: if supplied an iterable that has more than 2 members
        """
        return self._join_by

    @join_by.setter
    def join_by(self, value):
        self._join_by = None
        
    @property
    def rowsize(self) -> Optional[int]:
        """The row size - how many Y axis units each heatmap row should span. Defaults to
        ``1``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._rowsize

    @rowsize.setter
    def rowsize(self, value):
        self._rowsize = validators.integer(value,
                                           allow_empty = True,
                                           minimum = 1)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),
            
            'animation_limit': as_dict.get('animationLimit', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'colors': as_dict.get('colors', None),
            'curve_factor': as_dict.get('curveFactor', None),
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'line_width': as_dict.get('lineWidth', None),
            'marker_end': as_dict.get('markerEnd', None),
            'max_width': as_dict.get('maxWidth', None),
            'min_width': as_dict.get('minWidth', None),
            'null_color': as_dict.get('nullColor', None),
            'null_interaction': as_dict.get('nullInteraction', None),
            'weight': as_dict.get('weight', None),
            'width': as_dict.get('width', None),
            'z_index': as_dict.get('zIndex', None),

            'affects_map_view': as_dict.get('affectsMapView', None),

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'colsize': as_dict.get('colsize', None),
            'interpolation': as_dict.get('interpolation', None),
            'rowsize': as_dict.get('rowsize', None),

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        from highcharts_maps.utility_functions import mro__to_untrimmed_dict
        
        untrimmed = {
            'colsize': self.colsize,
            'interpolation': self.interpolation,
            'rowsize': self.rowsize,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

