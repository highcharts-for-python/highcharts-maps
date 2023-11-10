from typing import Optional, List

from validator_collection import validators, checkers

from highcharts_maps import errors
from highcharts_maps.decorators import class_sensitive, validate_types
from highcharts_maps.utility_classes.javascript_functions import (CallbackFunction,
                                                                  VariableName)

from highcharts_maps.options.series.data.map_data import MapData, AsyncMapData

from highcharts_core.options.chart import (PanningOptions,
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
    def map(self) -> Optional[str | MapData | AsyncMapData | VariableName | List[MapData | AsyncMapData]]:
        """:term:`Map geometries <map geometry>` that provide instructions on how to
        render the map itself, along with relevant properties used to join each map area
        to its corresponding values in the
        :meth:`MapSeriesBase.data <highcharts_maps.options.series.base.MapSeriesBase.data>`.

        Accepts (either in object representation or as coercable objects):

          * :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
          * :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          * :class:`VariableName <highcharts_maps.utility_classes.javascript_functions.VariableName>`
          * :class:`GeoJSONBase <highcharts_maps.utility_classes.geojson.GeoJSONBase>` or
            descendant
          * :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>`
          * a :class:`str <python:str>` URL, which will be coerced to
            :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          * a :class:`str <python:str>` number, which will act as an index to the
            (JavaScript) ``Highcharts.maps`` array

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>` or
          :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          or :obj:`None <python:None>`
        """
        return self._map

    @map.setter
    def map(self, value):
        if not value:
            self._map = None
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
            cleaned_value = []
            for item in value:
                if isinstance(item, (MapData, AsyncMapData, VariableName)):
                    item = item
                elif checkers.is_url(item):
                    item = AsyncMapData(url = item)
                elif checkers.is_integer(item, coerce_value = True):
                    item = item
                elif isinstance(item, dict) and 'url' in item:
                    item = AsyncMapData.from_dict(item)
                elif isinstance(item, str) and 'url:' in item:
                    item = AsyncMapData.from_json(item)
                elif checkers.is_type(item, 'GeoDataFrame'):
                    item = MapData.from_geodataframe(item)
                else:
                    try:
                        item = MapData.from_topojson(item)
                    except (ValueError, TypeError):
                        try:
                            item = MapData.from_geojson(item)
                        except (ValueError, TypeError):
                            raise errors.HighchartsValueError(
                                f'map expects a value '
                                f'that is str, TopoJSON, '
                                f'GeoJSON, a MapData '
                                f'object, an AsyncMapData '
                                f'object, or coercable to '
                                f'one. Received: '
                                f'{item.__class__.__name__}'
                            )
                cleaned_value.append(item)
            value = [x for x in cleaned_value]
        elif isinstance(value, (MapData, AsyncMapData)):
            value = value
        elif checkers.is_url(value):
            value = AsyncMapData(url = value)
        elif checkers.is_integer(value, coerce_value = True):
            value = value
        elif isinstance(value, dict) and 'url' in value:
            value = AsyncMapData.from_dict(value)
        elif isinstance(value, str) and 'url:' in value:
            value = AsyncMapData.from_json(value)
        elif checkers.is_type(value, 'GeoDataFrame'):
            value = MapData.from_geodataframe(value)
        else:
            try:
                value = MapData.from_topojson(value)
            except (ValueError, TypeError):
                try:
                    value = MapData.from_geojson(value)
                except (ValueError, TypeError):
                    try:
                        value = validate_types(value, VariableName)
                    except (ValueError, TypeError):
                        raise errors.HighchartsValueError(
                            f'map expects a value '
                            f'that is str, TopoJSON, '
                            f'GeoJSON, a MapData '
                            f'object, an AsyncMapData '
                            f'object, or coercable to '
                            f'one. Received: '
                            f'{value.__class__.__name__}'
                        )

        self._map = value

    @property
    def map_transforms(self) -> Optional[dict]:
        """Set of latitude/longitude transformation definitions
        for the chart. If :obj:`None <python:None>`, will be extracted automatically from
        the underlying :term:`map geometry`. Defaults to :obj:`None <python:None>`.

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

    @property
    def is_async(self) -> bool:
        """Read-only property which indicates whether the data visualization should be
        rendered using asynchronous logic.

        .. note::

          This property will only return ``True`` if one or more series rely on
          :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`

        :rtype: :class:`bool <python:bool>`
        """
        if checkers.is_iterable(self.map):
            for item in self.map:
                if isinstance(item, (AsyncMapData)):
                    return True
            return False

        if isinstance(self.map, AsyncMapData):
            return True

        return False