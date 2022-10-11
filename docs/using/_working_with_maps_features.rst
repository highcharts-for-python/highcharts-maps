.. tabs::

  .. tab:: Setting Up Your Map

    When configuring your map visualization, obviously you need to configure the actual
    "map" your visualization will be rendering. All maps are defined by their
    :term:`geometries <map geometry>`, which is a fancy way of saying they are defined
    by a very precise definition of the lines and shapes that make up the map.

    Typically, your map definition will be stored in either :term:`GeoJSON`,
    :term:`TopoJSON`, or ESRI :term:`Shapefile` files. **Highcharts for Maps** natively
    supports these formats, automatically rendering the maps defined by their content.

    The map used in your visualization can be defined in two separate places:

    .. tabs::

      .. tab:: in ``options.chart.map``

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

      .. tab:: in the series itself

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

    Your map itself is defined using either :term:`GeoJSON`, :term:`Topojson`, or
    :term:`Shapefiles <Shapefile>` formats. The most important decision you will need to
    make is whether you wish to load your map data synchronously within
    **Highcharts Maps for Python** and then supply the chart definition *and* the map
    definition to your (JavaScript) client, or whether you would prefer to load the map
    definition asynchronously from your (JavaScript) client:

    .. tip::

      **Best practice!**

      Because map data can be verbose and relatively large on the wire, we prefer to rely
      on the asynchronous method, but there are plenty of valid use cases where the
      synchronous approach is the best choice.

    .. tabs::

      .. tab:: Asynchronous Map Data

        You can configure your visualization to load your map data asynchronously by
        supplying an
        :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
        instance to either ``.options.chart.map`` or ``.map_data`` as described above.
        The
        :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
        instance contains a configuration that tells **Highcharts for Maps** how to have
        your (JavaScript) client download (using JavaScript's ``fetch()``) your map data.

        The
        :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
        instance is configured essentially by supplying it with three pieces of
        information:

          * The ``url`` from where your map data should be downloaded. This should be
            the URL to a single file which contains either :term:`GeoJSON`,
            :term:`Topojson`, or :term:`Shapefile` data.
          * An optional ``selector`` (JavaScript) function which you can use to have your
            (JavaScript) code modify, change, or sub-select data from your asynchronously
            fetched map file before rendering your chart.
          * An optional ``fetch_configuration`` which you can use to configure the details
            of how your (JavaScript) code will execute the (JavaScript) ``fetch()``
            request from the ``url`` (typically used to supply credentials against a
            backend API, for example).

        If you have configured an asynchronous map, **Highcharts for Maps** will
        automatically serialize it to JavaScript (when calling
        :meth:`Chart.to_js_literal() <highcharts_maps.chart.Chart.to_js_literal>`)
        using (JavaScript) ``async/await`` and the ``fetch()`` API.

        .. tip::

          **Best practice!**

          This approach is recommended because - in practice - it minimizes the amount
          of data transferred over the wire between your Python backend and your
          (JavaScript) client. This is particularly helpful because map
          :term:`geometries <map geometry>` can be verbose and occupy a (relatively)
          large amount of space on the wire.

      .. tab:: Synchronous Map Data

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

  .. tab:: Configuring the Map View

    Besides setting up your map itself, you can also configure the map view using the
    :meth:`HighchartsMapsOptions.map_view <highcharts_maps.options.HighchartsMapsOptions.map_view>`
    property. This property lets you use a
    :class:`MapViewOptions <highcharts_maps.options.map_views.MapViewOptions>` to
    configure:

      * any :term:`map insets <map inset>` that should be rendered on your map,
      * the default zoom settings for your map,
      * the default center / positioning for your map, and
      * any custom :term:`projection` that should be applied to your map to render
        it the way you want to.

    .. seealso::

      * :meth:`HighchartsMapsOptions.map_view <highcharts_maps.options.HighchartsMapsOptions.map_view>`
      * :class:`MapViewOptions <highcharts_maps.options.map_views.MapViewOptions>`

    **Map Insets**

      Map insets are particularly useful when you wish to render either non-contiguous
      areas (e.g. Alaska and Hawaii on a map of the United States of America) or to render
      a blown-up/zoomed-in section of the map with special options (think of this as a
      "detail section").

      You can configure general settings that will apply to all insets on your map using
      the
      :meth:`MapViewOptions.inset_options <highcharts_maps.options.map_views.MapViewOptions.inset_options>`
      property. And you can then supply the specific definition of each inset (which can
      override those general inset options) using the
      :meth:`MapViewOptions.insets <highcharts_maps.options.map_views.MapViewOptions.insets>`
      property and one or more
      :class:`Inset <highcharts_maps.options.map_views.insets.Inset>`
      instances.

      .. seealso::

        * :meth:`MapViewOptions.inset_options <highcharts_maps.options.map_views.MapViewOptions.inset_options>`
        * :meth:`MapViewOptions.insets <highcharts_maps.options.map_views.MapViewOptions.insets>`
        * :class:`InsetOptions <highcharts_maps.options.map_views.insets.InsetOptions>`
        * :class:`Inset <highcharts_maps.options.map_views.insets.Inset>`

    .. caution::

      It is important to note that unlike the rest of **Highcharts Maps for Python** and
      `Highcharts Maps <https://www.highcharts.com/products/maps/>`__, insets are
      defined using :term:`GeoJSON` geometries and *not* :term:`TopoJSON`.

      For more information, please see the documentation for the
      :class:`Inset <highcharts_maps.options.map_views.insets.Inset>` class.

    **Zoom Settings**

      You can configure your map's maximum zoom level using the
      :meth:`MapViewOptions.max_zoom <highcharts_maps.options.map_views.MapViewOptions.max_zoom>`
      property, and you can configure the default level of zoom using the
      :meth:`MapViewOptions.zoom <highcharts_maps.options.map_views.MapViewOptions.zoom>`
      setting.

    **Default Center**

      You can configure where your map will be centered by default using the
      :meth:`MapViewOptions.center <highcharts_maps.options.map_views.MapViewOptions.center>`
      property.

      .. seealso::

        * :meth:`MapViewOptions.center <highcharts_maps.options.map_views.MapViewOptions.center>`

    **Projection**

      All maps are :term:`projections <projection>` of a three-dimensional globe onto a
      two-dimensional plane (a map). Any such projection will in some ways distort the
      proportions of the areas depicted, and you may want to apply a different projection
      to better communicate insights from your data.

      Projections are configured using the
      :meth:`MapViewOptions.projection <highcharts_maps.options.map_views.MapViewOptions.projection>`
      property, which takes a
      :class:`ProjectionOptions <highcharts_maps.utility_classes.projections.ProjectionOptions>`
      instance.

      **Highcharts for Maps** supports both a number of built-in projections as well as
      providing the ability to apply a fully custom projection. The default projections
      supported are:

        * ``'EqualEarth'``
        * ``'LambertConformalConic'``
        * ``'Miller'``
        * ``'Orthographic'``
        * ``'WebMercator'``

      which can be compared using
      `Highcharts Projection Explorer demo <https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/maps/mapview/projection-explorer>`__

      If you wish to define a custom projection (which is calculated client-side in your
      JavaScript code), you can do so by supplying a
      :class:`CustomProjection <highcharts_maps.utility_classes.projections.CustomProjection>`
      instance to
      :class:`MapViewOptions.custom <highcharts_maps.options.map_views.MapViewOptions.custom>`.

      .. seealso::

        * :ref:`Using Custom Projections <custom_projections>`
        * `Highcharts Projection Explorer demo <https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/maps/mapview/projection-explorer>`__
        * :class:`ProjectionOptions <highcharts_maps.utility_classes.projections.ProjectionOptions>`
        * :class:`CustomProjection <highcharts_maps.utility_classes.projections.CustomProjection>`

  .. tab:: Configuring Map Navigation

    You can configure how users will navigate your map using the
    :meth:`HighchartsMapsOptions.map_navigation <highcharts_maps.options.HighchartsMapsOptions.map_navigation>`
    setting. It allows you to configure how the map zooms in and out in response to user
    behavior (clicks, double clicks, mouse wheel, etc.).

    .. seealso::

      :class:`MapNavigationOptions <highcharts_maps.options.map_navigation.MapNavigationOptions>`
