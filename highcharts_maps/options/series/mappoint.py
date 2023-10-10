from typing import Optional, List

from highcharts_maps.options.plot_options.mappoint import MapPointOptions
from highcharts_maps.options.series.base import MapSeriesBase
from highcharts_maps.options.series.data.geometric import GeometricLatLonData, GeometricLatLonDataCollection
from highcharts_maps.utility_functions import mro__to_untrimmed_dict, is_ndarray


class MapPointSeries(MapSeriesBase, MapPointOptions):
    """:term:`Map Points <Map Point>` are a special version of a scatter series where the
    points are positioned according to geographic coordinates within a map.

    .. figure:: ../../../_static/mappoint-example.png
      :alt: Map Point Example chart
      :align: center

    .. tip::

      **Best practice!**

      This can be very useful for rendering cities or other locations on your map.

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[GeometricLatLonData] | GeometricLatLonDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`GeometricLatLonData`
        instances, it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              my_series = MapPointSeries()
              my_series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a
            :meth:`.value <highcharts_maps.options.series.data.geometric.GeometricLatLonData.value>`-value,
            corresponding to the index of an area represented in the
            :meth:`.map_data <highcharts_maps.options.series.map.MapPointSeries.map_data>`.

          .. tab:: 2D Collection

            .. code-block::

              my_series = MapPointSeries()
              my_series.data = [
                  ['us-ny', 0],
                  ['us-mi', 5],
                  ['us-tx', 3],
                  ['us-ak', 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as the
            :meth:`.name <highcharts_maps.options.series.data.geometric.GeometricLatLonData.name>` and
            :meth:`.y <highcharts_maps.options.series.data.geometric.GeometricLatLonData.y>` pair.


            .. warning::

              If supplying a 2D collection, it is importnat that the ``name`` value map to
              matching map area values in the property indicated by
              :meth:`MapPointSeries.join_by <highcharts_maps.options.series.map.MapPointSeries.join_by>`,
              which defaults to ``'hc-key'``.

          .. tab:: Object Collection

            A one-dimensional collection of
            :class:`GeometricLatLonData <highcharts_maps.options.series.data.geometric.GeometricLatLonData>`
            objects.

        :rtype: :class:`list <python:list>` of
          :class:`GeometricLatLonData <highcharts_maps.options.series.data.geometric.GeometricLatLonData>`
          or :class:`GeometricLatLonDataCollection`
          or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = GeometricLatLonData.from_array(value)

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

            'cluster': as_dict.get('cluster', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
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
        return GeometricLatLonDataCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return GeometricLatLonData
