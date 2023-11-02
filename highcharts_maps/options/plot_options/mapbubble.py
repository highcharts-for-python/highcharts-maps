from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.options.plot_options.bubble import BubbleOptions

from highcharts_maps.options.plot_options.base import MapBaseOptions
from highcharts_maps.utility_functions import validate_color, mro__to_untrimmed_dict
from highcharts_maps.utility_classes.gradients import Gradient
from highcharts_maps.utility_classes.patterns import Pattern


class MapBubbleOptions(MapBaseOptions, BubbleOptions):
    """Map Bubble charts are :term:`maps <map>` where the numerical value is depicted as a
    bubble rendered over the corresponding area of the map rather than as a color.

    .. figure:: ../../../_static/mapbubble-example.png
      :alt: Map Bubble Example chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._data_as_columns = None
        self._line_color = None

        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.data_as_columns = kwargs.get('data_as_columns', None)
        self.line_color = kwargs.get('line_color', None)

        super().__init__(**kwargs)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each area of the map. Defaults to
        ``'#cccccc'``.

        :rtype: :class:`str <python:str>` or
          :class:`Gradient <highcharts_maps.utility_classes.gradients.Gradient>` or
          :class:`Pattern <highcharts_maps.utility_classes.patterns.Pattern>` or
          :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = validate_color(value)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding each area of the map. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def data_as_columns(self) -> Optional[bool]:
        """If ``True``, indicates that the data is structured as columns instead of as
        rows. Defaults to :obj:`None <python:None>`, which behaves as ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._data_as_columns

    @data_as_columns.setter
    def data_as_columns(self, value):
        if value is None:
            self._data_as_columns = None
        else:
            self._data_as_columns = bool(value)

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """Color of the line connecting bubbles. If :obj:`None <python:None>`, defaults to
        the same color as the series color.

        :rtype: :class:`str <python:str>` or
          :class:`Gradient <highcharts_maps.utility_classes.gradients.Gradient>` or
          :class:`Pattern <highcharts_maps.utility_classes.patterns.Pattern>` or
          :obj:`None <python:None>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        self._line_color = validate_color(value)

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
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'inactive_other_points': as_dict.get('inactiveOtherPoints', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'display_negative': as_dict.get('displayNegative', None),
            'jitter': as_dict.get('jitter', None),
            'max_size': as_dict.get('maxSize', None),
            'min_size': as_dict.get('minSize', None),
            'size_by': as_dict.get('sizeBy', None),
            'size_by_absolute_value': as_dict.get('sizeByAbsoluteValue', None),
            'z_max': as_dict.get('zMax', None),
            'z_min': as_dict.get('zMin', None),
            'z_threshold': as_dict.get('zThreshold', None),

            'all_areas': as_dict.get('allAreas', None),
            'join_by': as_dict.get('joinBy', None),

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
            'line_color': as_dict.get('lineColor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'dataAsColumns': self.data_as_columns,
            'lineColor': self.line_color,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
