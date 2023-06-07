from typing import Optional

from highcharts_maps.options.plot_options.map import MapOptions
from highcharts_maps.utility_functions import validate_color, mro__to_untrimmed_dict
from highcharts_maps.utility_classes.gradients import Gradient
from highcharts_maps.utility_classes.patterns import Pattern


class MapLineOptions(MapOptions):
    """Map Lines are a special version of a :term:`map` series where the value affects the
    the strokes (borders) shown on the map, rather than the area fills.

    .. figure:: ../../../_static/mapline-example.png
      :alt: Mapline Example chart
      :align: center

    .. tip::

      **Best practice!**

      This can be useful for applying free-form drawing within a map, or for rendering
      geometric features like rivers or mountains in your map.

    """

    def __init__(self, **kwargs):
        self._fill_color = None

        self.fill_color = kwargs.get('fill_color', None)

        super().__init__(**kwargs)

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """Fill color of the map line shapes. Defaults to ``'none'``.

        :rtype: :class:`str <python:str>` or
          :class:`Gradient <highcharts_maps.utility_classes.gradients.Gradient>` or
          :class:`Pattern <highcharts_maps.utility_classes.patterns.Pattern>` or
          :obj:`None <python:None>`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        self._fill_color = validate_color(value)

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
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'negative_color': as_dict.get('negativeColor', None),

            'all_areas': as_dict.get('allAreas', None),
            'join_by': as_dict.get('joinBy', None),

            'affects_map_view': as_dict.get('affectsMapView', None),
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
            'null_color': as_dict.get('nullColor', None),
            'null_interaction': as_dict.get('nullInteraction', None),

            'fill_color': as_dict.get('fillColor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'fillColor': self.fill_color
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
