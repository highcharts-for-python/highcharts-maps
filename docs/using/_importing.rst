.. tabs::

  .. tab:: from Precise Location

    .. tip::

      **Best Practice!**

      This method of importing **Highcharts Maps for Python** objects yields the fastest
      performance for the ``import`` statement. However, it is more verbose and requires
      you to navigate the extensive :doc:`Highcharts Maps for Python API </api>`.

    .. code-block:: python

      # Import classes using precise module indications. For example:
      from highcharts_maps.chart import Chart
      from highcharts_maps.global_options.shared_options import SharedMapsOptions
      from highcharts_maps.options import HighchartsMapsOptions
      from highcharts_maps.options.plot_options.map import MapOptions
      from highcharts_maps.options.series.map import MapSeries

  .. tab:: from ``.highcharts``

    .. caution::

      This method of importing **Highcharts Maps for Python** classes has relatively slow
      performance because it imports hundreds of different classes from across the entire
      library. This performance impact may be acceptable to you in your use-case, but
      do use at your own risk.

    .. code-block:: python

      # Import objects from the catch-all ".highcharts" module.
      from highcharts_maps import highcharts

      # You can now access specific classes without individual import statements.
      highcharts.Chart
      highcharts.SharedMapsOptions
      highcharts.HighchartsMapsOptions
      highcharts.MapOptions
      highcharts.MapSeries
