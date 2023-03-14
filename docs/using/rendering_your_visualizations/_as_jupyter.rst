.. code-block:: python

  from highcharts_maps.chart import Chart
  from highcharts_maps.options.series.area import LineSeries
  from highcharts_maps.global_options.shared_options import SharedStockOptions

  my_chart = Chart(container = 'target_div',
                   options = {
                       'series': [
                           LineSeries(data = [0, 5, 3, 5])
                       ]
                   },
                   variable_name = 'myChart',
                   is_maps_chart = True)

  # Now this will render the contents of "my_chart" in your Jupyter Notebook
  my_chart.display()

  # You can also supply shared options to display to make sure that they are applied:
  my_shared_options = SharedStockOptions()

  # Now this will render the contents of "my_chart" in your Jupyter Notebook, but applying
  # your shared options
  my_chart.display(global_options = my_shared_options)

.. collapse:: Method Signature

  .. method:: display(self, global_options = None)
    :noindex:

    Display the chart in `Jupyter Labs <https://jupyter.org/>`__ or
    `Jupyter Notebooks <https://jupyter.org/>`__.

    :param global_options: The :term:`shared options` to use when rendering the chart.
      Defaults to :obj:`None <python:None>`
    :type global_options: :class:`SharedOptions <highcharts_maps.global_options.shared_options.SharedOptions>`
      or :obj:`None <python:None>`

    :raises HighchartsDependencyError: if
      `ipython <https://ipython.readthedocs.io/en/stable/>`__ is not available in the
      runtime environment
