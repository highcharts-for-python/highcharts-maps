You can configure your visualization to load your map data asynchronously by
supplying an
:class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
instance to either ``.options.chart.map`` or ``.map_data`` as described above.

The
:class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
instance contains a configuration that tells **Highcharts Maps for Python** how to have
your (JavaScript) client download (using JavaScript's ``fetch()``) your map data.

The
:class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
instance is configured by supplying it with three pieces of information:

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

If you have configured an asynchronous map, **Highcharts Maps for Python** will
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
