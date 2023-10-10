#############################################
Quickstart: Patterns and Best Practices
#############################################

.. contents::
  :depth: 2
  :backlinks: entry

----------------------

******************
Installation
******************

.. include:: _installation.rst

----------------------

*****************************************************
Importing Highcharts Maps for Python Objects
*****************************************************

.. include:: using/_importing.rst

-------------------

*****************************************************
Standardizing Your Charts
*****************************************************

.. tabs::

  .. tab:: Shared Options

    .. tabs::

      .. tab:: with JS Literal

         .. include:: using/shared_options/_with_js_literal.rst

      .. tab:: with JSON

         .. include:: using/shared_options/_with_json.rst

      .. tab:: with :class:`dict <python:dict>`

         .. include:: using/shared_options/_with_dict.rst

  .. tab:: Templates

    .. tabs::

      .. tab:: via JS Literal

        .. include:: using/templates/_with_js_literal.rst

      .. tab:: via ``.copy()``

        .. include:: using/templates/_with_copy.rst

      .. tab:: via :class:`dict <python:dict>`

        .. include:: using/templates/_with_dict.rst

---------------------

************************************
Populating Series with Data
************************************

Configuring Your Map Data
================================

.. tabs::

  .. tab:: w/ ``options.chart.map``

    .. include:: using/configuring_map_data/_with_chart_map.rst

  .. tab:: w/ ``<Series>.map_data``

    .. include:: using/configuring_map_data/_with_series_map_data.rst

  .. tab:: using ``AsyncMapData``

    .. include:: using/configuring_map_data/_using_async_map_data.rst

  .. tab:: using ``MapData``

    .. include:: using/configuring_map_data/_using_synchronous_map_data.rst

Populating the Series Data
================================

.. tabs::

  .. tab:: w/ ``.data``

    .. include:: using/populating_series_data/_with_data_property.rst

  .. tab:: from Array

    .. tabs::
      
      .. tab:: Create a New Series

        .. include:: using/populating_series_data/_new_from_array.rst

      .. tab:: Update an Existing Series

        .. include:: using/populating_series_data/_load_from_array.rst


  .. tab:: from GeoPandas

    .. tabs::

      .. tab:: Create a New Series

        .. include:: using/populating_series_data/_new_from_geopandas.rst

      .. tab:: Update an Existing Series

        .. include:: using/populating_series_data/_load_from_geopandas.rst

  .. tab:: from CSV

    .. tabs::

      .. tab:: Create a New Series

        .. include:: using/populating_series_data/_new_from_csv.rst

      .. tab:: Update an Existing Series

        .. include:: using/populating_series_data/_load_from_csv.rst

  .. tab:: from Pandas

    .. tabs::

      .. tab:: Create a New Series

        .. include:: using/populating_series_data/_new_from_pandas.rst

      .. tab:: Update an Existing Series

        .. include:: using/populating_series_data/_load_from_pandas.rst

  .. tab:: from PySpark

    .. tabs::

      .. tab:: Create a New Series

        .. include:: using/populating_series_data/_new_from_pyspark.rst

      .. tab:: Update an Existing Series

        .. include:: using/populating_series_data/_load_from_pyspark.rst

------------------------

************************************
Assembling Your Chart and Options
************************************

.. tabs::

  .. tabs:: Using Keyword Arguments

    .. include:: using/assembling_your_chart/_using_kwargs.rst

  .. tab:: Using ``.add_series()``

    .. include:: using/assembling_your_chart/_using_add_series.rst

  .. tab:: Using ``.from_geopandas()``

    .. include:: using/assembling_your_chart/_using_from_geopandas.rst

  .. tab:: Using ``.from_series()``

    .. include:: using/assembling_your_chart/_using_from_series.rst

  .. tab:: Using ``.series``

    .. include:: using/assembling_your_chart/_using_series_property.rst

--------------

**********************************
Rendering Your Visualizations
**********************************

.. tabs::

  .. tab:: As Web Content

    .. include:: using/rendering_your_visualizations/_as_web_content.rst

  .. tab:: in Jupyter Labs or Jupyter Notebook

    .. include:: using/rendering_your_visualizations/_as_jupyter.rst

-------------------------

***************************************************
Downloading a Rendered Highcharts Visualization
***************************************************

.. tabs::

  .. tab:: Using Highsoft's Export Server

    .. include:: using/download_visualizations/_using_highsoft.rst

  .. tab:: Using a Custom Export Server

    .. include:: using/download_visualizations/_using_custom.rst

----------------------

************************************
Using Highcharts Maps Features
************************************

.. include:: using/_working_with_maps_features.rst
