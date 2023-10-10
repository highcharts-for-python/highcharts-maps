.. code-block:: python

  # Given a geoPandas DataFrame instance named "gdf"
  from highcharts_maps.chart import Chart

  my_chart = Chart.from_geopandas(gdf,
                                  property_map = {
                                      'id': 'state',
                                      'value': 'value'
                                  },
                                  series_type = 'map')


.. collapse:: Method Signature

  .. seealso::

    * :meth:`MapSeriesBase.from_geopandas() <highcharts_maps.options.series.base.MapSeriesBase.from_geopandas>`

  .. method:: .from_geopandas(cls, df, property_map, series_type, series_kwargs = None, options_kwargs = None, chart_kwargs = None)
    :noindex:
    :classmethod:

    Create a :class:`Chart <highcharts_maps.chart.Chart>` instance whose
    data is populated from a `geopandas <https://geopandas.org/>`__
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

    :param series_type: Indicates the series type that should be created from the data
      in ``gdf``.
    :type series_type: :class:`str <python:str>`

    :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
      arguments that should be used when instantiating the series instance. Defaults
      to :obj:`None <python:None>`.

      .. warning::

        If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
        The ``data`` value will be created from ``gdf`` instead.

    :type series_kwargs: :class:`dict <python:dict>`

    :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
      arguments that should be used when instantiating the :class:`HighchartsOptions`
      instance. Defaults to :obj:`None <python:None>`.

      .. warning::

        If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
        *overwritten*. The ``series`` value will be created from the data in ``gdf``.

    :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

    :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
      arguments that should be used when instantiating the :class:`Chart` instance.
      Defaults to :obj:`None <python:None>`.

      .. warning::

        If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
        *overwritten*. The ``options`` value will be created from the
        ``options_kwargs`` and the data in ``gdf`` instead.

    :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

    :returns: A :class:`Chart <highcharts_maps.chart.Chart>` instance with its
      data populated from the data in ``gdf``.
    :rtype: :class:`Chart <highcharts_maps.chart.Chart>`

    :raises HighchartsPandasDeserializationError: if ``property_map`` references
      a column that does not exist in the data frame
    :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`__ is
      not available in the runtime environment
