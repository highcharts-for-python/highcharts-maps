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

        .. include:: /using/configuring_map_data/_with_chart_map.rst

      .. tab:: in the series itself

        .. include:: /using/configuring_map_data/_with_series_map_data.rst

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

        .. include:: /using/configuring_map_data/_using_async_map_data.rst

      .. tab:: Synchronous Map Data

        .. include:: /using/configuring_map_data/_using_synchronous_map_data.rst
        
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
      the ability to apply a fully custom projection. The default projections
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
