from typing import Optional, List

from highcharts_maps.decorators import class_sensitive
from highcharts_maps.options.plot_options.flowmap import FlowmapOptions, GeoHeatmapOptions
from highcharts_maps.options.series.base import SeriesBase
from highcharts_maps.options.series.data.connections import FlowmapData, FlowmapDataCollection
from highcharts_maps.options.series.data.geometric import GeometricLatLonData
from highcharts_maps.utility_functions import mro__to_untrimmed_dict, is_ndarray


class FlowmapSeries(SeriesBase, FlowmapOptions):
    """A :term:`flowmap` series is a series laid out on top of a map series that displays route paths (e.g. flight 
    or naval routes), or directional flows on a map. It creates a link between two points on a map chart.
    
    .. figure:: ../../../_static/flowmap-example.png
      :alt: Flowmap Example chart
      :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[FlowmapData] | FlowmapDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`FlowmapData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 3D Collection

            .. code-block::

              my_series = FlowmapSeries()
              my_series.data = ['Point 1', 'Point 2', 4]

            A three-dimensional collection of values, where the first member corresponds to the origin point,
            the second member corresponds to the destination point, and the third member represents the weight given
            to the connection. 

          .. tab:: Object Collection

            A one-dimensional collection of
            :class:`FlowmapData <highcharts_maps.options.series.data.connections.FlowmapData>`
            objects.

        :rtype: :class:`list <python:list>` of
          :class:`FlowmapData <highcharts_maps.options.series.data.connections.FlowmapData>`
          or :class:`FlowmapDataCollection`
          or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = FlowmapData.from_array(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
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
            
            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),

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
        return FlowmapDataCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return FlowmapData


class GeoHeatmapSeries(FlowmapSeries, GeoHeatmapOptions):
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
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[GeometricLatLonData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`GeometricLatLonData`
        instances, it accepts as input the following types of data:

        .. tabs::

          .. tab:: Object Collection

            A one-dimensional collection of
            :class:`GeometricLatLonData <highcharts_maps.options.series.data.geometric.GeometricLatLonData>`
            objects.

        :rtype: :class:`list <python:list>` of
          :class:`GeometricLatLonData <highcharts_maps.options.series.data.geometric.GeometricLatLonData>`
          or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    @class_sensitive(GeometricLatLonData, force_iterable = True)
    def data(self, value):
        self._data = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
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
            
            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),

            'affects_map_view': as_dict.get('affectsMapView', None),

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'colsize': as_dict.get('colsize', None),
            'interpolation': as_dict.get('interpolation', None),
            'rowsize': as_dict.get('rowsize', None),

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls)

        return untrimmed
