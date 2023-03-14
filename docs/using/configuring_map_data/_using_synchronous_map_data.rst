You can supply your map :term:`geometries <map geometry>` directly within Python
as well, and that map data will then be serialized to JavaScript along with your
chart definition when you call
:meth:`Chart.to_js_literal() <highcharts_maps.chart.Chart.to_js_literal>`.

Synchronous map data is represented as a
:class:`MapData <highcharts_maps.options.series.data.map_data.MapData>` instance.
This object can most easily be created by calling one of its deserializer methods:

  * :meth:`.from_topojson() <highcharts_maps.options.series.data.map_data.MapData.from_topojson>`
  * :meth:`.from_geojson() <highcharts_maps.options.series.data.map_data.MapData.from_geojson>`
  * :meth:`.from_geodataframe() <highcharts_maps.options.series.data.map_data.MapData.from_geodataframe>`
  * :meth:`.from_shapefile() <highcharts_maps.options.series.data.map_data.MapData.from_shapefile>`

Each of these class methods will return a
:class:`MapData <highcharts_maps.options.series.data.map_data.MapData>` instance
whose
:meth:`.topology <highcharts_maps.options.series.data.map_data.MapData.topology>`
property will now be populated with your :term:`map geometry`.

.. tabs::

  .. tab:: ``.from_topojson()``

    .. code-block:: python

      from highcharts_maps.options.series.data.map_data import MapData

      # Load Map Data from a TopoJSON file
      my_map_data = MapData.from_topojson('my-map-data.topo.json')

      # Load Map Data from a TopoJSON string "my_topojson_string"
      my_map_data = MapData.from_topojson(my_topojson_string)

  .. tab:: ``.from_geojson()``

    .. code-block:: python

      from highcharts_maps.options.series.data.map_data import MapData

      # Load Map Data from a GeoJSON file
      my_map_data = MapData.from_geojson('my-map-data.geo.json')

      # Load Map Data from a GeoJSON string "my_geojson_string"
      my_map_data = MapData.from_geojson(my_geojson_string)

  .. tab:: ``.from_geodataframe()``

    .. code-block:: python

      from highcharts_maps.options.series.data.map_data import MapData

      # Load Map Data from a GeoPandas GeoDataFrame "gdf"
      my_map_data = MapData.from_geodataframe(gdf)

  .. tab:: ``.from_shapefile()``

    .. code-block:: python

      from highcharts_maps.options.series.data.map_data import MapData

      # Load Map Data from an ESRI Shapefile
      my_map_data = MapData.from_shapefile('my-shapefile.shp')

      # Load Map Data from an ESRI Shapefile ZIP
      my_map_data = MapData.from_shapefile('my-shapefile.zip')


.. note::

  The :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
  instance will *automatically* convert your :term:`map geometry` to
  :term:`TopoJSON`. This is useful because :term:`TopoJSON` is a much more
  compact format than :term:`GeoJSON` which minimizes the amount of data
  transferred over the wire.

  If you absolutely *need* to have GeoJSON delivered to your (JavaScript) client,
  you can force GeoJSON on serialization by setting the
  :meth:`MapData.force_geojson <highcharts_maps.options.series.data.map_data.MapData.force_geojson>`
  property to ``True`` (it defaults to ``False``).
