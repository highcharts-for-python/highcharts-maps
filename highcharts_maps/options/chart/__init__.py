from typing import Optional, List

from validator_collection import validators, checkers

from highcharts_maps import errors
from highcharts_maps.decorators import class_sensitive, validate_types
from highcharts_maps.utility_classes.javascript_functions import CallbackFunction

from highcharts_maps.utility_classes.map_data import MapDataOptions
from highcharts_maps.utility_classes.geojson import GeoJSON
from highcharts_maps.utility_classes.topojson import TopoJSON

from highcharts_python.options.chart import (PanningOptions,
                                             ChartOptions as ChartOptionsBase)


class ChartOptions(ChartOptionsBase):
    """Configuration settings that apply to a chart."""

    def __init__(self, **kwargs):
        self._map = None
        self._map_transforms = None
        self._proj4 = None

        self.map = kwargs.get('map', None)
        self.map_transforms = kwargs.get('map_transforms', None)
        self.proj4 = kwargs.get('proj4', None)

    @property
    def map(self) -> Optional[int | str | List[MapDataOptions] | GeoJSON | TopoJSON]:
        """Default :term:`map data` for all series, expressed either as:

          * an index to the (JavaScript) ``Highcharts.maps`` array
          * a collection of :class:`MapDataOptions <highcharts_maps.utility_classes.map_data.MapDataOptions>`
            instances
          * a :class:`GeoJSON <highcharts_maps.utility_classes.geojson.GeoJSON>` instance
          * a :class:`TopoJSON <highcharts_maps.utility_classes.topojson.TopoJSON>`
            instance

        Defaults to :obj:`None <python:None>`.

        .. tip::

          For determining individual shapes and geometries to use for each series, please
          see :meth:`series.map_data <highcharts_maps.options.series.map_data>`.

        :rtype: :class:`int <python:int>` or :class:`str <python:str>` or
          :class:`GeoJSON <highcharts_maps.utility_classes.geojson.GeoJSON>` or
          :class:`TopoJSON <highcharts_maps.utility_classes.topjson.TopoJSON>` or
          :class:`list <python:list>` of
          :class:`MapDataOptions <highcharts_maps.utility_classes.map_data.MapDataOptions>`
          or :obj:`None <python:None>`
        """
        return self._map

    @map.setter
    def map(self, value):
        if not value:
            self._map = None
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
            value = validate_types(MapDataOptions, force_iterable = True)
        else:
            try:
                value = validators.integer(value, coerce_value = True)
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, GeoJSON)
                except (ValueError, TypeError):
                    try:
                        value = validate_types(value, TopoJSON)
                    except (ValueError, TypeError):
                        raise errors.HighchartsValueError(f'map must either be None, an '
                                                          f'int, GeoJSON, TopoJSON, or a '
                                                          f'collection of MapDataOptions'
                                                          f'instances. Was: '
                                                          f'{value.__class__.__name__}')

            self._map = value

    @property
    def map_transforms(self) -> Optional[dict]:
        """Set of latitude/longitude :term:`transformation <transformation>` definitions
        for the chart. If :obj:`None <python:None>`, will be extracted automatically from
        the underlying :term:`map data`. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._map_transforms

    @map_transforms.setter
    def map_transforms(self, value):
        if not value:
            self._map_transforms = None
        else:
            self._map_transforms = validators.dict(value)

    @property
    def proj4(self) -> Optional[CallbackFunction]:
        """Function which can be used to manually load the `proj4 <http://proj4js.org/>`__
        JavaScript library which
        `Highcharts Maps <https://www.highcharts.com/products/maps/>`__ depends on.
        Defaults to :obj:`None <python:None>`, which assumes that the
        `proj4 <http://proj4js.org/>`__ library is loaded via (HTML) ``<script/>`` tag.

        :rtype: :class:`CallbackFunction <highcharts_maps.utility_classes.javascript_functions.CallbackFunction>`
          or :obj:`None <python:None>`
        """
        return self._proj4

    @proj4.setter
    @class_sensitive(CallbackFunction)
    def proj4(self, value):
        self._proj4 = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align_thresholds': as_dict.get('alignThresholds', None),
            'align_ticks': as_dict.get('alignTicks', None),
            'allow_mutating_data': as_dict.get('allowMutatingData', None),
            'animation': as_dict.get('animation', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color_count': as_dict.get('colorCount', None),
            'display_errors': as_dict.get('displayErrors', None),
            'events': as_dict.get('events', None),
            'height': as_dict.get('height', None),
            'ignore_hidden_series': as_dict.get('ignoreHiddenSeries', None),
            'inverted': as_dict.get('inverted', None),
            'margin': as_dict.get('margin', None),
            'margin_bottom': as_dict.get('marginBottom', None),
            'margin_left': as_dict.get('marginLeft', None),
            'margin_right': as_dict.get('marginRight', None),
            'margin_top': as_dict.get('marginTop', None),
            'number_formatter': as_dict.get('numberFormatter', None),
            'options_3d': as_dict.get('options3d', None),
            'pan_key': as_dict.get('panKey', None),
            'panning': as_dict.get('panning', None),
            'parallel_axes': as_dict.get('parallelAxes', None),
            'parallel_coordinates': as_dict.get('parallelCoordinates', None),
            'plot_background_color': as_dict.get('plotBackgroundColor', None),
            'plot_background_image': as_dict.get('plotBackgroundImage', None),
            'plot_border_color': as_dict.get('plotBorderColor', None),
            'plot_border_width': as_dict.get('plotBorderWidth', None),
            'plot_shadow': as_dict.get('plotShadow', None),
            'polar': as_dict.get('polar', None),
            'reflow': as_dict.get('reflow', None),
            'render_to': as_dict.get('renderTo', None),
            'scrollable_plot_area': as_dict.get('scrollablePlotArea', None),
            'selection_marker_fill': as_dict.get('selectionMarkerFill', None),
            'shadow': as_dict.get('shadow', None),
            'show_axes': as_dict.get('showAxes', None),
            'spacing': as_dict.get('spacing', None),
            'spacing_bottom': as_dict.get('spacingBottom', None),
            'spacing_left': as_dict.get('spacingLeft', None),
            'spacing_top': as_dict.get('spacingTop', None),
            'spacing_right': as_dict.get('spacingRight', None),
            'style': as_dict.get('style', None),
            'styled_mode': as_dict.get('styledMode', None),
            'type': as_dict.get('type', None),
            'width': as_dict.get('width', None),
            'zooming': as_dict.get('zooming', None),

            'map': as_dict.get('map', None),
            'map_transforms': as_dict.get('mapTransforms', None),
            'proj4': as_dict.get('proj4', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'map': self.map,
            'mapTransforms': self.map_transforms,
            'proj4': self.proj4
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
