You can supply your map :term:`geometries <map geometry>` directly within Python
as well, and that map data will then be serialized to JavaScript along with your
chart definition when you call
:meth:`Chart.to_js_literal() <highcharts_maps.chart.Chart.to_js_literal>`.

Within **Highcharts Maps for Python**, synchronous map data is represented as a
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

    .. seealso::

      * :meth:`MapData.from_topojson() <highcharts_maps.options.series.data.map_data.MapData.from_topojson>`

    .. collapse:: Method Signature

      .. method:: .from_topojson(cls, as_topojson_or_file: str | bytes, allow_snake_case: bool = True)
        :noindex:
        :classmethod:

        Construct an instance of the class from a :term:`TopoJSON` string.

        :param as_topojson_or_file: The :term:`TopoJSON` string for the object or the
          filename of a file that contains the TopoJSON string.
        :type as_topojson_or_file: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_topojson_or_file``.
        :rtype: :class:`MapData`

  .. tab:: ``.from_geojson()``

    .. code-block:: python

      from highcharts_maps.options.series.data.map_data import MapData

      # Load Map Data from a GeoJSON file
      my_map_data = MapData.from_geojson('my-map-data.geo.json')

      # Load Map Data from a GeoJSON string "my_geojson_string"
      my_map_data = MapData.from_geojson(my_geojson_string)

    .. seealso::

      * :meth:`MapData.from_geojson() <highcharts_maps.options.series.data.map_data.MapData.from_geojson>`

    .. collapse:: Method Signature

      .. method:: .from_geojson(cls, as_geojson_or_file: str | bytes, allow_snake_case: bool = True)
        :noindex:
        :classmethod:

        Construct an instance of the class from a GeoJSON string.

        :param as_geojson_or_file: The :term:`GeoJSON` string for the object or the
          filename of a file that contains the GeoJSON string.
        :type as_geojson_or_file: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_geojson_or_file``.
        :rtype: :class:`MapData`

  .. tab:: ``.from_geodataframe()``

    .. code-block:: python

      from highcharts_maps.options.series.data.map_data import MapData

      # Load Map Data from a GeoPandas GeoDataFrame "gdf"
      my_map_data = MapData.from_geodataframe(gdf)

    .. seealso::

      * :meth:`MapData.from_geodataframe() <highcharts_maps.options.series.data.map_data.MapData.from_geodataframe>`

    .. collapse:: Method Signature

      .. method:: .from_geodataframe(cls, as_gdf, prequantize = False, \*\*kwargs)
        :noindex:
        :classmethod:

        Create a :class:`MapData` instance from a
        :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`.

        :param as_gdf: The :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`
          containing the :term:`map geometry`.
        :type as_gdf: :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`

        :param prequantize: If ``True``, will perform the TopoJSON optimizations
          ("quantizing the topology") before generating the :class:`Topology` instance.
          Defaults to ``False``.
        :type prequantize: :class:`bool <python:bool>`
        
        :param kwargs: additional keyword arguments which are passed to the
          :class:`Topology` constructor
        :type kwargs: :class:`dict <python:dict>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`

  .. tab:: ``.from_shapefile()``

    .. code-block:: python

      from highcharts_maps.options.series.data.map_data import MapData

      # Load Map Data from an ESRI Shapefile
      my_map_data = MapData.from_shapefile('my-shapefile.shp')

      # Load Map Data from an ESRI Shapefile ZIP
      my_map_data = MapData.from_shapefile('my-shapefile.zip')

    .. seealso::

      * :meth:`MapData.from_shapefile() <highcharts_maps.options.series.data.map_data.MapData.from_shapefile>`

    .. collapse:: Method Signature

      .. method:: .from_shapefile(cls, shp_filename)
        :noindex:
        :classmethod:

        Create a :class:`MapData` instance from an :term:`ESRI Shapefile <shapefile>`.

        :param shp_filename: The full filename of an :term:`ESRI Shapefile <shapefile>`
          to load.

          .. note::

            :term:`ESRI Shapefiles <shapefile>` are actually composed of three files each,
            with one file receiving the ``.shp`` extension, one with a ``.dbf`` extension,
            and one (optional) file with a ``.shx`` extension.

            **Highcharts Maps for Python** will resolve all three files given a single
            base filename. Thus:

              ``/my-shapefiles-folder/my_shapefile.shp``

            will successfully load data from the three files:

              ``/my-shapefiles-folder/my_shapefile.shp``
              ``/my-shapefiles-folder/my_shapefile.dbf``
              ``/my-shapefiles-folder/my_shapefile.shx``

          .. tip::

            **Highcharts for Python** will also correctly load and unpack
            :term:`shapefiles <shapefile>` that are grouped together within a ZIP file.

        :type shp_filename: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`


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
