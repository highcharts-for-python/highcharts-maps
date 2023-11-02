from typing import Optional, List

from highcharts_maps.options.plot_options.mapbubble import MapBubbleOptions
from highcharts_maps.options.series.base import MapSeriesBase
from highcharts_maps.utility_functions import mro__to_untrimmed_dict, is_ndarray
from highcharts_maps.options.series.data.geometric import GeometricZData, GeometricZDataCollection


class MapBubbleSeries(MapSeriesBase, MapBubbleOptions):
    """:term:`Map Bubble` charts are :term:`maps <map>` where the numerical value is
    depicted as a bubble rendered over the corresponding area of the map rather than as a
    color.

    .. figure:: ../../../_static/mapbubble-example.png
      :alt: Map Bubble Example chart
      :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[GeometricZData] | GeometricZDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`GeometricZData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              my_series = MapBubbleSeries()
              my_series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a
            :meth:`.z <highcharts_maps.options.series.data.geometric.GeometricZData.z>`-value,
            corresponding to the index of an area represented in the
            :meth:`.map_data <highcharts_maps.options.series.map.MapSeries.map_data>`.

          .. tab:: 2D Collection

            .. code-block::

              my_series = MapBubbleSeries()
              my_series.data = [
                  ['us-ny', 0],
                  ['us-mi', 5],
                  ['us-tx', 3],
                  ['us-ak', 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as the
            :meth:`.name <highcharts_maps.options.series.data.geometric.GeometricZData.name>` and
            :meth:`.z <highcharts_maps.options.series.data.geometric.GeometricZData.z>` pair.

            .. warning::

              If supplying a 2D collection, it is importnat that the ``name`` value map to
              matching map area values in the property indicated by
              :meth:`MapBubbleSeries.join_by <highcharts_maps.options.series.mapbubble.MapBubbleSeries.join_by>`,
              which defaults to ``'hc-key'``.

          .. tab:: Object Collection

            A one-dimensional collection of
            :class:`GeometricZData <highcharts_maps.options.series.data.geometric.GeometricZData>`
            objects.

        :rtype: :class:`list <python:list>` of
          :class:`GeometricZData <highcharts_maps.options.series.data.geometric.GeometricZData>`
          or :class:`GeometricZDataCollection`
          or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = GeometricZData.from_array(value)

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

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'map_data': as_dict.get('mapData', None),

            'all_areas': as_dict.get('allAreas', None),
            'join_by': as_dict.get('joinBy', None),

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
            'line_color': as_dict.get('lineColor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls)

        return untrimmed

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return GeometricZDataCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return GeometricZData
