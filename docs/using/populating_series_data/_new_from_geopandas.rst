.. note::

  The ``.from_geopandas()`` method is available on all :term:`series` classes which
  support rendering as a map visualization. This includes:

    * :class:`MapSeries <highcharts_maps.options.series.map.MapSeries>`
    * :class:`MapBubbleSeries <highcharts_maps.options.series.mapbubble.MapBubbleSeries>`
    * :class:`MapLineSeries <highcharts_maps.options.series.mapline.MapLineSeries>`
    * :class:`MapPointSeries <highcharts_maps.options.series.mappoint.MapPointSeries>`
    * :class:`HeatmapSeries <highcharts_maps.options.series.heatmap.HeatmapSeries>`
    * :class:`TilemapSeries <highcharts_maps.options.series.tilemap.TilemapSeries>`

  allowing you to either assemble a series or an entire chart from a GeoPandas
  :class:`GeoDataFrame <geopandas:GeoDataFrame>` with only one method call.

.. code-block:: python

  # Given a geoPandas DataFrame instance named "gdf"
  from highcharts_maps.chart import Chart
  from highcharts_maps.options.series.map import MapSeries

  # Creating a Series from the GeoDataFrame
  my_series = MapSeries.from_geopandas(gdf,
                                       property_map = {
                                           'id': 'state',
                                           'value': 'value'
                                       })

  # Creating a Chart with a MapSeries from the GeoDataFrame.
  my_chart = Chart.from_geopandas(gdf,
                                  property_map = {
                                      'id': 'state',
                                      'value': 'value'
                                  },
                                  series_type = 'map')


.. collapse:: Method Signature

  .. seealso::

    * :meth:`Chart.from_geopandas() <highcharts_maps.chart.Chart.from_geopandas>`

  .. method:: .from_geopandas(cls, df, property_map, series_kwargs = None)
    :noindex:
    :classmethod:

    Create a :term:`series` instance whose
    :meth:`.data <highcharts_maps.options.series.base.SeriesBase.data>` property
    is populated from a `geopandas <https://geopandas.org/>`__
    :class:`GeoDataFrame <geopandas:GeoDataFrame>`.

    :param gdf: The :class:`GeoDataFrame <geopandas:GeoDataFrame>` from which data
      should be loaded.
    :type gdf: :class:`GeoDataFrame <geopandas:GeoDataFrame>`

    :param property_map: A :class:`dict <python:dict>` used to indicate which
      data point property should be set to which column in ``gdf``. The keys in the
      :class:`dict <python:dict>` should correspond to properties in the data point
      class, while the value should indicate the label for the
      :class:`GeoDataFrame <geopandas:GeoDataFrame>` column.
    :type property_map: :class:`dict <python:dict>`

    :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
      arguments that should be used when instantiating the series instance. Defaults
      to :obj:`None <python:None>`.

      .. warning::

        If ``series_kwargs`` contains a ``data`` or ``map_data`` key, their values
        will be *overwritten*. The ``data`` and ``map_data`` values will be created
        from ``gdf`` instead.

    :type series_kwargs: :class:`dict <python:dict>`

    :returns: A :term:`series` instance (descended from
      :class:`MapSeriesBase <highcharts_maps.options.series.base.MapSeriesBase>`) with
      its :meth:`.data <highcharts_maps.options.series.base.SeriesBase.data>` and
      :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>`
      properties from the data in ``gdf```
    :rtype: :class:`list <python:list>` of series instances (descended from
      :class:`MapSeriesBase <highcharts_maps.options.series.base.MapSeriesBase>`)

    :raises HighchartsPandasDeserializationError: if ``property_map`` references
      a column that does not exist in the data frame
    :raises HighchartsDependencyError: if `geopandas <https://geopandas.pydata.org/>`__
      is not available in the runtime environment
