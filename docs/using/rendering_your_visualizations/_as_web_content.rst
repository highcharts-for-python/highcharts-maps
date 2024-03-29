.. tabs::

  .. tab:: as a Highcharts Maps Chart

    .. code-block:: python

      from highcharts_maps.chart import Chart
      from highcharts_maps.options.series.hlc import HLCSeries

      my_chart = Chart(container = 'target_div',
                       options = {
                           'series': [
                               HLCSeries(data = [
                                   [2, 0, 4],
                                   [4, 2, 8],
                                   [3, 9, 3]
                               ])
                           ]
                       },
                       variable_name = 'myChart',
                       is_maps_chart = True)

      as_js_literal = my_chart.to_js_literal()

      # This will produce a string equivalent to:
      #
      # document.addEventListener('DOMContentLoaded', function() {
      #   const myChart = Highcharts.stockChart('target_div', {
      #      series: {
      #          type: 'hlc',
      #          data: [
      #            [2, 0, 4],
      #            [4, 2, 8],
      #            [3, 9, 3]
      #          ]
      #      }
      #   });
      # });

  .. tab:: as a Highcharts JS Chart

    .. code-block:: python

      from highcharts_maps.chart import Chart
      from highcharts_maps.options.series.area import LineSeries

      my_chart = Chart(data = [0, 5, 3, 5], series_type = 'line')

      as_js_literal = my_chart.to_js_literal()

      # This will produce a string equivalent to:
      #
      # document.addEventListener('DOMContentLoaded', function() {
      #   const myChart = Highcharts.chart('target_div', {
      #      series: {
      #          type: 'line',
      #          data: [0, 5, 3, 5]
      #      }
      #   });
      # });
