from typing import Optional

from highcharts_core.options.plot_options.pie import (VariablePieOptions,
                                                        PieOptions as PieOptionsBase)

from highcharts_maps.utility_functions import mro__to_untrimmed_dict
from highcharts_maps.options.plot_options.base import MapBaseOptions


class PieOptions(MapBaseOptions, PieOptionsBase):
    """General options to apply to all Pie series types.

    A pie chart is a circular graphic which is divided into slices to illustrate
    numerical proportion.

    .. tabs::

      .. tab:: Pie Chart

        .. figure:: ../../../_static/pie-example.png
          :alt: Pie Example Chart
          :align: center

      .. tab:: Donut Chart

        .. figure:: ../../../_static/pie-example-donut.png
          :alt: Donut Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._data_as_columns = None

        self.data_as_columns = kwargs.get('data_as_columns', None)

        super().__init__(**kwargs)

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

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'center': as_dict.get('center', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'colors': as_dict.get('colors', None),
            'depth': as_dict.get('depth', None),
            'end_angle': as_dict.get('endAngle', None),
            'fill_color': as_dict.get('fillColor', None),
            'ignore_hidden_point': as_dict.get('ignoreHiddenPoint', None),
            'inner_size': as_dict.get('innerSize', None),
            'linecap': as_dict.get('linecap', None),
            'min_size': as_dict.get('minSize', None),
            'size': as_dict.get('size', None),
            'sliced_offset': as_dict.get('slicedOffset', None),
            'start_angle': as_dict.get('startAngle', None),
            'thickness': as_dict.get('thickness', None),

            'all_areas': as_dict.get('allAreas', None),
            'join_by': as_dict.get('joinBy', None),

            'data_as_columns': as_dict.get('dataAsColumns', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dataAsColumns': self.data_as_columns,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
