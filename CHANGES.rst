Release 1.2.0
=========================================

* **ENHANCEMENT:** Align the API to **Highcharts (JS) v.11.1** (#21). In particular, this includes:

  * Changes inherited from **Highcharts Core for Python v.1.2.0**. See `here <https://core-docs.highchartspython.com/en/latest/history.html#release-1-2-0>`__.
  * Added ``TiledWebMapOptions`` / ``TiledWebMapSeries`` support.
  
* **ENHANCEMENT:** Added support for the inclusion of scripts based on features used in the chart (#6).
* **ENHANCEMENT:** Added ``dict`` support to ``options.series.labels.SeriesLabel.style`` and ``utility_classes.data_labels.DataLabel.style``.
* **BUGFIX:** Fixed de-serialization error in ``options.series.data.geometric.GeometricZData`` which
  prevented the population of ``.properties``.
* **DOCS:** Several documentation fixes.
* **DEPENDENCY:** Bumped ``requests`` version for security patch.

---------------------

Release 1.1.1
=========================================

* **FIXED:** Problem when producing a JS literal, with the JS code inserting an unnecessary ``new``.
* **ENHANCEMENT:** Added more elegant error handling when something goes wrong displaying a chart in Jupyter.

---------------------

Release 1.1.0
=========================================

* Align the API to **Highcharts (JS) v.11**. In particular, this includes:

  * Changes inherited from **Highcharts Core for Python v.1.1.0**. See `here <https://core-docs.highchartspython.com/en/latest/history.html#release-1-1-0>`__.
  * Added ``options.drilldown.Drilldown.map_zooming`` property.
  * Added ``FlowmapOptions`` / ``FlowmapSeries`` support.
  * Added ``GeoHeatmapOptions`` / ``GeoHeatmapSeries`` support.

* **FIXED:** Fixed missing ``TreegraphOptions`` / ``TreegraphSeries`` series type.

---------------

Release 1.0.1
=========================================

* Added documentation of "hard" dependencies to the README.
* Fixed broken links in documentation to ``options.plot_options.heatmap.HeatmapOptions`` 
  and ``options.plot_options.heatmap.TilemapOptions``.

---------------

Release 1.0.0
=========================================

* **First official release!**

---------------

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

