When defining a map series (descended from
:class:`MapSeriesBase <highcharts_maps.options.series.base.MapSeriesBase>`, e.g.
:class:`MapSeries <highcharts_maps.options.series.map.MapSeries>` or
:class:`MapBubbleSeries <highcharts_maps.options.series.mapbubble.MapBubbleSeries>`),
you can configure the map in the series
:meth:`.map_data <highcharts_maps.options.series.base.MapSeriesbase.map_data>`
property.

As with ``options.chart.map``, this property takes either a
:class:`MapData <highcharts_maps.options.series.data.map_data.MapData>` instance
or an
:class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
instance which contains the :term:`GeoJSON`, :term:`TopoJSON`, or
:term:`Shapefile` definition of your :term:`map geometry`.
