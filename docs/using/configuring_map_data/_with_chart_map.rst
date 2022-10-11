When configuring your visualization, you can set your chart's basic configuration
settings in the :meth:`Chart.options <highcharts_maps.chart.Chart.options>`
option, specifically in the
:meth:`Chart.options.chart <highcharts_maps.options.chart.ChartOptions>` property.
There, you will find the
:meth:`ChartOptions.map <highcharts_maps.options.chart.ChartOptions.map>` property
which is where you supply your map definition.

This property accepts either a
:class:`MapData <highcharts_maps.options.series.data.map_data.MapData>` instance
or an
:class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
instance which contains the :term:`GeoJSON`, :term:`TopoJSON`, or
:term:`Shapefile` definition of your :term:`map geometry`.

The map defined in this property will be the default map used for all series
rendered on your chart. Since most map visualizations will be rendering all series
on one map, this is the most common use case.

.. tip::

  **Best practice!**

  It is recommended to use ``options.chart.map`` to configure your visualization's
  map. This is because laying out a single visualization that has multiple series
  represented on multiple maps is a very complicated configuration, and is
  rarely necessary.
