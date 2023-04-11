Release 1.0.0-rc6
=========================================

* Fixed bug in deserialization of ``options.plot_options.base.MapBaseOptions.join_by``.
* Fixed Heatmap and Highcharts Maps JavaScript import conflict.
* Fixed bug in utility_classes.projections.ProjectionOptions.custom property.
* Fixed serialization bugs in options.series.data.map_data.MapData.
* Added ``properties`` support to data point classes in ``options.series.data.geometric``.
* Updated Jupyter display logic to align with **Highcharts Core for Python** signatures.
* Added demos to documentation.

---------------

Release 1.0.0-rc5
=========================================

* Further tweaks to documentation CSS for better accessibility.

---------------

Release 1.0.0-rc4
=========================================

* Added CSS overrides to documentation for better accessibility.
* Added jQuery to documentation to address issue in Sphinx 6.0 and Sphinx RTD Theme.

----------------------

Release 1.0.0-rc3
=========================================

* Fixed unneeded ``python-dotenv`` dependency.
* Fixed JSON deserialization in ``.from_array()``.
* Added ``options.chart.ChartOptions.is_async`` property.
* Updated ``utility_classes.fetch_configuration.FetchConfiguration`` serialization to handle quote escaping.
* Fixed JS literal synchronization when ``options.chart.map`` is asynchronous.

--------------

Release 1.0.0-rc2
=========================================

* Revised documentation.

--------------

Release 1.0.0-rc1
=========================================

* First public release: **Release Candidate 1**

