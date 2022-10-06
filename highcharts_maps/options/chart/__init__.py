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

        super().__init__(**kwargs)

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

    @property
    def type(self) -> Optional[str]:
        """The default series type for the chart. Defaults to ``'map'``.

        Can be any of the chart types listed under :class:`PlotOptions` and
        :class:`Series`, or can be a series provided by an additional module.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        self._type = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
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
            'map': as_dict.get('map', None),
            'map_transforms': as_dict.get('mapTransforms', None),
            'margin': as_dict.get('margin', None),
            'margin_bottom': as_dict.get('marginBottom', None),
            'margin_left': as_dict.get('marginLeft', None),
            'margin_right': as_dict.get('marginRight', None),
            'margin_top': as_dict.get('marginTop', None),
            'number_formatter': as_dict.get('numberFormatter', None),
            'pan_key': as_dict.get('panKey', None),
            'panning': as_dict.get('panning', None),
            'plot_background_color': as_dict.get('plotBackgroundColor', None),
            'plot_background_image': as_dict.get('plotBackgroundImage', None),
            'plot_border_color': as_dict.get('plotBorderColor', None),
            'plot_border_width': as_dict.get('plotBorderWidth', None),
            'plot_shadow': as_dict.get('plotShadow', None),
            'proj4': as_dict.get('proj4', None),
            'reflow': as_dict.get('reflow', None),
            'render_to': as_dict.get('renderTo', None),
            'selection_marker_fill': as_dict.get('selectionMarkerFill', None),
            'shadow': as_dict.get('shadow', None),
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
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'allowMutatingData': self.allow_mutating_data,
            'animation': self.animation,
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'colorCount': self.color_count,
            'displayErrors': self.display_errors,
            'events': self.events,
            'height': self.height,
            'map': self.map,
            'mapTransforms': self.map_transforms,
            'margin': self.margin,
            'marginBottom': self.margin_bottom,
            'marginLeft': self.margin_left,
            'marginRight': self.margin_right,
            'marginTop': self.margin_top,
            'numberFormatter': self.number_formatter,
            'panKey': self.pan_key,
            'panning': self.panning,
            'plotBackgroundColor': self.plot_background_color,
            'plotBackgroundImage': self.plot_background_image,
            'plotBorderColor': self.plot_border_color,
            'plotBorderWidth': self.plot_border_width,
            'plotShadow': self.plot_shadow,
            'proj4': self.proj4,
            'reflow': self.reflow,
            'renderTo': self.render_to,
            'selectionMarkerFill': self.selection_marker_fill,
            'shadow': self.shadow,
            'spacing': self.spacing,
            'spacingBottom': self.spacing_bottom,
            'spacingLeft': self.spacing_left,
            'spacingRight': self.spacing_right,
            'spacingTop': self.spacing_top,
            'style': self.style,
            'styledMode': self.styled_mode,
            'type': self.type,
            'width': self.width,
            'zooming': self.zooming,
        }

        return untrimmed
