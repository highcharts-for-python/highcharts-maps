.. code-block:: python

  # Given a MapSeries named "my_series", and a GeoPandas DataFrame variable named "gdf"
  my_series.load_from_geopandas(gdf,
                                property_map = {
                                    'id': 'id',
                                    'value': 'value'
                                })

.. collapse:: Method Signature

  .. method:: .load_from_geopandas(self, gdf, property_map)
    :noindex:

    Replace the contents of the
    :meth:`.data <highcharts_maps.options.series.base.SeriesBase.data>` property
    with data points and the
    :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>`
    property with geometries populated from a `geopandas <https://geopandas.org/>`__
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

    :raises HighchartsPandasDeserializationError: if ``property_map`` references
      a column that does not exist in the data frame
    :raises HighchartsDependencyError: if `geopandas <https://geopandas.org/>`__ is
      not available in the runtime environment
