.. note::

  **Highcharts Maps for Python** has several types of dependencies:

    * "hard" dependencies, without which you will not be able to use the library at all,
    * "soft" dependencies, which will not produce errors but which may limit the value you
      get from the library,
    * "developer" dependencies that contributors will need in their local environment, and
    * "documentation" dependencies that are necessary if you wish to generate (this)
      documentation

.. tabs::

  .. tab:: Hard

    .. warning::

      If these hard dependencies are not available in the environment where
      **Highcharts Maps for Python** is running, then the library will simply not work.
      Besides `Highcharts Maps <https://www.highcharts.com/products/maps>`__ itself, all
      of the other hard dependencies are automatically installed when installing
      **Highcharts Maps for Python**.

    * `Highcharts Maps <https://www.highcharts.com/products/maps/>`__ v.10.2 or higher

      .. note::

        Not technically a Python dependency, but obviously **Highcharts Maps for Python**
        will not work properly if your rendering layer does not leverage Highcharts Maps.

    * `highcharts-python <https://highcharts-python.readthedocs.io>`_ v.1.0.0 or higher
    * `esprima-python <https://github.com/Kronuz/esprima-python>`_ v.4.0 or higher
    * `requests <https://requests.readthedocs.io/en/latest/>`_ v.2.28 or higher
    * `validator-collection <https://validator-collection.readthedocs.io/en/latest/>`_
      v.1.5 or higher
    * `topojson <https://mattijn.github.io/topojson/>`_ v.1.5 or higher
    * `geojson <https://github.com/jazzband/geojson/>`_ v.2.5 or higher

  .. tab:: Soft

    .. warning::

      If these soft dependencies are not available in the environment where
      **Highcharts Maps for Python** is running, then the library will throw a
      :exc:`HighchartsDependencyError <errors.HighchartsDependencyError>` exception when
      you try to use functionality that relies on them.

      No error will be thrown until you try to use dependent functionality. So for
      example, if you call a ``from_pandas()`` method but
      `pandas <https://pandas.pydata.org/>`_ is not installed, you will get an error.

    * `geopandas <https://geopandas.org/en/stable/>`_ v. 0.11 or higher
    * `pandas <https://pandas.pydata.org/>`_ v. 1.3 or higher
    * `PyShp <https://github.com/GeospatialPython/pyshp>`__ v.2.3.1 or higher
    * `pyspark <https://spark.apache.org/docs/latest/api/python/index.html>`_ v.3.3 or
      higher
    * `python-dotenv <https://github.com/theskumar/python-dotenv>`_ v. 0.21 or higher

      .. note::

        `python-dotenv <https://github.com/theskumar/python-dotenv>`_ will fail silently if
        not available, as it will only leverage natural environment variables rather than
        a ``.env`` file in the runtime environment.

  .. tab:: Developer

    .. warning::

      You will not be able to run unit tests without the Pytest test framework and a
      number of necessary extensions. To install the developer (and documentation)
      dependencies, execute:

      .. code-block:: bash

        $ pip install highcharts-maps[develop]

    * `pytest <https://docs.pytest.org/en/7.1.x/>`_ v.7.1 or higher
    * `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/>`_ v.3.0 or higher
    * `pytest-xdist <https://pytest-xdist.readthedocs.io/en/latest/>`_ v.2.5 or higher

  .. tab:: Documentation

    .. warning::

      You will not be able to generate documentation without Sphinx and a number of
      necessary extensions. To install the documentation dependencies, execute:

      .. code-block:: bash

        $ pip install highcharts-maps[docs]

    * `Sphinx <https://www.sphinx-doc.org/en/master/>`_ v.5.1 or higher
    * `Sphinx RTD Theme <https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/>`_ v.1.0
      or higher
    * `sphinx-tabs <https://sphinx-tabs.readthedocs.io/>`_ v.3.4.1 or higher
    * `Sphinx Toolbox <https://sphinx-toolbox.readthedocs.io/en/latest/>`_ v.3.2 or higher
