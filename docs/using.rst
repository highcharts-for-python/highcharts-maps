#####################################
Using Highcharts Maps for Python
#####################################

.. contents::
  :depth: 3
  :backlinks: entry

--------------

*******************************************************************
Introduction to Highcharts Maps and Highcharts for Python
*******************************************************************

.. sidebar:: The Highcharts for Python Toolkit

  The **Highcharts Maps for Python** library is part of the broader
  `Highcharts for Python Toolkit <https://www.highcharts.com/integrations/python>`__, 
  which together provides comprehensive support across the entire 
  `Highcharts <https://www.highcharts.com>`__ suite of data visualization libraries.

  **Highcharts Maps for Python** extends the functionality of
  `Highcharts Core for Python <https://core-docs.highchartspython.com/>`__, providing 
  support for `Highcharts Maps (JS) <https://www.highcharts.com/products/maps>`__ in the same way that
  Highcharts Maps (JS) extends 
  `Highcharts Core (JS) <https://www.highcharts.com/products/highcharts/>`__.

  .. note::

    **Highcharts Maps for Python** is an *additive* extension to
    `Highcharts Core for Python <https://core-docs.highchartspython.com/>`__:

      * It includes the full set of functionality from Highcharts Core for Python.
      * It is fully bakcwards-compatible with Highcharts Core for Python.
      * It exposes the exact same API for you to use. 
      
    This makes it easy to for you to combine visualization from the
    `Highcharts Core <https://www.highcharts.com/products/highcharts/>`__ library *and* the
    `Highcharts Maps <https://www.highcharts.com/products/maps/>`_ library without
    wrangling multiple similar dependencies in your Python code.

`Highcharts Maps <https://www.highcharts.com/products/maps/>`__  is the gold-standard
in JavaScript data visualization libraries for map and
:iabbr:`GIS (Geographic Information System)` data, enabling you to design rich, beautiful, 
and highly interactive data visualizations of (almost) any kind imaginable, and to render 
those visualizations in your web or mobile applications. Take a look at some of the
`customer showcases <https://www.highcharts.com/blog/posts/highcharts-maps+use-cases/>`_
and `demo gallery <https://www.highcharts.com/products/maps/demo>`_ to see some examples 
of what you can do with Highcharts Maps.

**Highcharts Maps for Python** is a Python wrapper for the
`Highcharts Maps <https://www.highcharts.com/products/maps/>`__ JavaScript library,
which means that it is designed to give developers working in Python a simple and Pythonic
way of interacting with Highcharts Maps (JS). 

**Highcharts Maps for Python** will *not* render data visualizations itself - that's what 
Highcharts Maps (JS) does - but it *will* allow you to:

  #. Configure your data visualizations in Python.
  #. Supply data you have in Python to your data visualizations.
  #. Programmatically produce the Highcharts Maps JavaScript code that will actually
     render your data visualization.
  #. Programmatically download a static version of your visualization (as needed) within
     Python.

.. tip::

  Think of **Highcharts Maps for Python** as a translator to bridge your data
  visualization needs between Python and JavaScript.

-------------------

*****************************************************
Key Design Patterns in Highcharts for Python
*****************************************************

`Highcharts <https://www.highcharts.com>`__ is a large, robust, and complicated JavaScript 
library. If in doubt, take a look at its extensive 
`documentation <https://www.highcharts.com/docs/index>`_ and in particular its 
`API reference`_. 

Because the **Highcharts for Python Toolkit** wraps the Highcharts (JS) API, its design is 
heavily shaped by Highcharts JS' own design - as one should expect.

However, one of the main goals of the Python toolkit is to make it easier for Python
developers to leverage the Highcharts JavaScript libraries - in particular by providing a 
more Pythonic way of interacting with the framework. 

Here are the notable design patterns that have been adopted that you should be aware of:

Code Style: Python vs JavaScript Naming Conventions
=======================================================

.. include:: using/_code_style_naming_conventions.rst

Standard Methods
=======================================

Every single object supported by the Highcharts Maps API corresponds to a Python class in
**Highcharts Maps for Python**. You can find the complete list in our comprehensive
:doc:`Highcharts Maps for Python API Reference <api>`.

These classes generally inherit from the
:class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` metaclass, which
provides each class with a number of standard methods. These methods are the "workhorses"
of **Highcharts Maps for Python** and you will be relying heavily on them when
using the library. Thankfully, their signatures and behavior is generally consistent -
even if what happens "under the hood" is class-specific at times.

The standard methods exposed by the classes are:

.. _using_deserialization_methods:

Deserialization Methods
---------------------------

.. include:: api/_deserialization_methods.rst

.. _using_serialization_methods:

Serialization Methods
--------------------------

.. include:: api/_serialization_methods.rst

.. _using_other_methods:

Other Convenience Methods
------------------------------

.. include:: api/_other_convenience_methods.rst

.. _handling_defaults:

Handling Default Values
===============================

.. include:: api/_handling_defaults.rst

Module Structure
=====================

.. include:: api/_module_structure.rst

Class Structures and Inheritance
====================================

.. include:: api/_class_structures.rst

.. warning::

  Certain sections of the **Highcharts Maps for Python** library - in particular the
  :mod:`options.series <highcharts_maps.options.series>` classes - rely heavily on
  multiple inheritance. This is a known anti-pattern in Python development as it runs the
  risk of encountering the :term:`diamond of death` inheritance problem. This complicates
  the process of inheriting methods or properties from parent classes when properties or
  methods share names across multiple parents.

  We know the diamond of death is an anti-pattern, but it was a necessary one to minimize 
  code duplication and maximize consistency. For that reason, we implemented it properly 
  *despite* the anti-pattern, using some advanced Python concepts to navigate the Python MRO
  (Method Resolution Order) system cleanly. However, an awareness of the pattern used
  may prove helpful if your code inherits from the Highcharts for Python classes.

  .. seealso::

    For a more in-depth discussion of how the anti-pattern was implemented safely and
    reliably, please review the :doc:`Contributor Guidelines <contributing>`.

--------------------------

*******************************************************
Organizing Your Highcharts for Python Project
*******************************************************

**Highcharts Maps for Python** is a utility that can integrate with - quite literally -
any frontend framework. Whether your Python application is relying on iPython (e.g.
`Jupyter Notebook`_ or `Jupyter Labs`_),
`Flask <https://flask.palletsprojects.com/en/2.2.x/>`_,
`Django <https://www.djangoproject.com/>`_,  `FastAPI <https://fastapi.tiangolo.com/>`_,
`Pyramid <https://trypyramid.com/>`_, `Tornado <https://www.tornadoweb.org/en/stable/>`_,
or some completely home-grown solution all Highcharts Maps for
Python needs is a place where
`Highcharts Maps <https://www.highcharts.com/products/maps/>`__ JavaScript code can be executed.

All of those frameworks mentioned have their own best practices for organizing their
application structures, and those should *always* take priority. Even in a data-centric
application that will be relying heavily on **Highcharts Maps for Python**, your
application's core business logic will be doing most of the heavy lifting and so your
project's organization should reflect that.

All of those frameworks mentioned have their own best practices for organizing their
application structures, and those best practices should *always* take priority. Even in a 
data-centric application that will be relying heavily on **Highcharts for Python**, your 
application's core business logic will be doing most of the heavy lifting and so your 
project's organization should reflect that.

However, there are a number of best practices that we recommend for organizing your
files and code to work with the **Highcharts for Python Toolkit**:

  .. warning::

      *There are nine and sixty ways of constructing a tribal lay, and every single one of
      them is right!* -- Rudyard Kipling, *In the Neolithic Age*

    The organizational model described below is just a suggestion, and you can (and likely
    will) depart from its principles and practices as you gain more experience using
    **Highcharts Maps for Python**. There's nothing wrong with that! It's just a set of
    best practices that we've found work for us and which we therefore recommend.

.. _importing:

Importing Highcharts Maps for Python
=========================================

.. include:: using/_importing.rst

.. _shared_options:

Use Shared Options
========================

One of the most challenging aspects of
`Highcharts Core <https://www.highcharts.com/products/highcharts/>`__ and
`Highcharts Maps <https://www.highcharts.com/products/maps/>`__ are their sheer breadth
of functionality and configurability. That's simultaneously their greatest strength,
and their greatest weakness. This is because it can be quite challenging to wrangle
thousands of properties - especially when even a single visualization can use hundreds of
those properties!

This is a challenge that we are keenly aware of, and one which we've given some thought to in 
the design of the **Highcharts for Python Toolkit**. A core principle you should use throughout 
your project is to practice :iabbr:`DRY (Do Not Repeat Yourself)` programming. 

If your application will be generating multiple visualizations, they will likely need some 
consistent configurations.

For example, you will want their title position to be consistent, their color schemes to
be consistent, their font sizing to be consistent, etc. In your code you want these
configuration settings to be defined *once* and then applied to all of the visualizations
you are producing.

This can be facilitated using the
:class:`SharedMapsOptions <highcharts_maps.global_options.shared_options.SharedMapsOptions>`
class. This generates a single set of global options which - when serialized to
JavaScript - apply its configuration settings consistently across all data
visualizations on the same page.

.. warning::

  :class:`SharedMapsOptions <highcharts_maps.global_options.shared_options.SharedMapsOptions>`
  is a sub-class of
  :class:`SharedOptions <highcharts_maps.global_options.shared_options.SharedOptions>`
  which extends its properties and methods with properties/methods that are only available
  in the `Highcharts Maps API <https://api.highcharts.com/highmaps/>`__.

  However, this class is fully backwards-compatible with the
  `Highcharts Core API <https://api.highcharts.com/highcharts/>`__ if you leave the
  Maps-specific methods and properties set to :obj:`None <python:None>` (their default).

As with all **Highcharts for Python** objects, you can instantiate them in several ways:

.. tabs::

  .. tab:: with JS Literal

    .. include:: using/shared_options/_with_js_literal.rst

  .. tab:: with JSON

    .. include:: using/shared_options/_with_json.rst

  .. tab:: with ``dict``

    .. include:: using/shared_options/_with_dict.rst

  .. tab:: with ``__init__()``

    You can also instantiate a
    :class:`SharedMapsOptions <highcharts_maps.global_options.shared_options.SharedMapsOptions>`
    instance directly using keywords in the constructor:

      .. code-block:: python

        from highcharts_maps.highcharts import ChartOptions, SharedMapsOptions

        my_shared_options = SharedMapsOptions(chart = ChartOptions(background_color = '#fff',
                                                                   border_width = 2,
                                                                   plot_background_color = 'rgba(255, 255, 255, 0.9)',
                                                                   plot_border_width = 1))

        js_code_snippet = my_shared_options.to_js_literal()

      .. note::

        You can also supply :class:`dict <python:dict>` representations as keyword argument
        values in the object constructors.

      .. tip::

        **Best practice!**

        While you can create a
        :class:`SharedMapsOptions <highcharts_maps.global_options.shared_options.SharedMapsOptions>`
        instance and then modify its properties after the fact, that's not exactly the best
        code style. It makes things a bit verbose, and a little harder to reason about.

        Instead, it's recommended that you instantiate your object with all of its
        properties in one go. If you need to change them later, you can do so using Python
        easily - but best to create it all at once.

Use Templates to Get Started
==================================

While :ref:`shared options <shared_options>` are applied to all charts that are rendered
on the same web page with the shared options JS code, certain types of visualizations
may need special treatment. Sure, you can use the
:meth:`plot_options <SharedOptions.plot_options>` settings to configure chart
type-specific options, but how can you efficiently use multiple charts of the same type
that have different settings?

For example, let's say you used :ref:`shared options <shared_options>` to set universal
bar chart settings. But what happens if you know you'll have different data shown in
different bar charts? You can use a similar templating pattern for different sub-types
of your charts.

.. tabs::

  .. tab:: with JS Literal

    .. include:: using/templates/_with_js_literal.rst

  .. tab:: with JSON

    .. include:: using/templates/_with_json.rst

  .. tab:: with ``dict``

    .. include:: using/templates/_with_dict.rst

  .. tab:: with ``.copy()``

    .. include:: using/templates/_with_copy.rst

-----------------

*************************************************
Working with Highcharts Maps Features
*************************************************

`Highcharts Maps <https://www.highcharts.com/products/maps/>`__ extends 
`Highcharts Core <https://www.highcharts.com/products/highcharts/>`__ with 
numerous features that add significant interactivity to your visualizations. 
These key features include:

.. include:: using/_working_with_maps_features.rst

-----------------

.. _working_with_data:

**************************************
Working with Data
**************************************

Obviously, if you are going to use **Highcharts Maps for Python** and
`Highcharts Maps <https://www.highcharts.com/product/maps/>`__ you will
need to have data to visualize. Python is rapidly becoming the *lingua franca* in the
world of data manipulation, transformation, and analysis and
**Highcharts Maps for Python** is specifically designed to play well within that
ecosystem to make it easy to visualize data from CSV files, from `geopandas`_ 
geodataframes, from ESRI Shapefiles, from `pandas`_ dataframes, or `PySpark`_ 
dataframes.

How Data is Represented
==================================

`Highcharts <https://www.highcharts.com>`__ (JS) supports two different ways of 
representing data: as an individual :term:`series` comprised of individual data 
points, and as a set of instructions to read data dynamically from a CSV file or 
an HTML table.

  .. seealso::

    * :class:`DataBase <highcharts_maps.options.series.data.base.DataBase>` class
    * :class:`options.Data <highcharts_maps.options.data.Data>` class

`Highcharts <https://www.highcharts.com>`__ organizes data into :term:`series`. You 
can think of a series as a single line on a graph that shows a set of values. The set 
of values that make up the series are :term:`data points <data point>`, which are defined 
by a set of properties that indicate the data point's position on one or more axes. 

As a result, `Highcharts (JS) <https://www.highcharts.com>`__ and
**Highcharts for Python** both represent the data points in series as a list of data point
objects in the ``data`` property within the series:

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - Highcharts JS
    - Highcharts for Python
  * - .. code-block:: javascript

        // Example Series Object
        // (for a Line series type):
        {
          data: [
            {
              id: 'first-data-point',
              x: 1,
              y: 123,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            },
            {
              id: 'second-data-point',
              x: 2,
              y: 456,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            },
            {
              id: 'third-data-point',
              x: 3,
              y: 789,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            }
          ],
          // ...
          // other Series properties go here
          // to configure styling/behavior
        }

    - .. code-block:: python

        # Corresponding LineSeries object
        my_series = Series(data = [
            CartesianData(id = 'first-data-point1',
                          x = 1,
                          y = 123),
            CartesianData(id = 'second-data-point1',
                          x = 2,
                          y = 456),
            CartesianData(id = 'third-data-point1',
                          x = 3,
                          y = 789),
        ])

As you can see, **Highcharts for Python** represents its data the same way that
`Highcharts (JS) <https://www.highcharts.com>`__ does. That should be expected. 
However, constructing tens, hundreds, or possibly thousands of data points 
individually in your code would be a nightmare. For that reason, the 
**Highcharts for Python Toolkit** provides a number of convenience methods to make it
easier to populate your series.

.. _populating_series_data:

Populating Series Data
===========================

Every single :term:`Series` class in **Highcharts Maps for Python** features several
different methods to either instantiate data points directly, load data (to an existing
series instance), or to create a new series instance with data already loaded.

.. tabs::

  .. tab:: Direct Instantiation

    When working with a :term:`series` instance, you can instantiate data points directly.
    These data points are stored in the
    :meth:`.data <highcharts_maps.options.series.base.SeriesBase.data>` setting, which
    always accepts/expects a list of data point instances (descended from
    :class:`DataBase <highcharts_maps.options.series.data.base.DataBase>`).

    Data points all have the same standard **Highcharts for Python**
    :ref:`deserialization methods <deserialization_methods>`, so those make things very easy.
    However, they also have a special data point-specific deserialization method:

      .. collapse:: Expand Method Signature

        .. method:: .from_array(cls, value)
          :classmethod:
          :noindex:

          Creates a collection of data point instances, parsing the contents of ``value`` as an
          array (iterable). This method is specifically used to parse data that is input to
          **Highcharts for Python** without property names, in an array-organized structure as
          described in the `Highcharts JS <https://www.highcharts.com>`__ documentation.

          .. seealso::

            The specific structure of the expected array is highly dependent on the type of data
            point that the series needs, which itself is dependent on the series type itself.

            Please review the detailed :ref:`series documentation <series_documentation>` for
            series type-specific details of relevant array structures.

          .. note::

            An example of how this works for a simple
            :class:`LineSeries <highcharts_maps.options.series.area.LineSeries>` (which uses
            :class:`CartesianData <highcharts_maps.options.series.data.cartesian.CartesianData>`
            data points) would be:

            .. code-block:: python

              my_series = LineSeries()

              # A simple array of numerical values which correspond to the Y value of the data
              # point
              my_series.data = [0, 5, 3, 5]

              # An array containing 2-member arrays (corresponding to the X and Y values of the
              # data point)
              my_series.data = [
                  [0, 0],
                  [1, 5],
                  [2, 3],
                  [3, 5]
              ]

              # An array of dict with named values
              my_series.data = [
                {
                    'x': 0,
                    'y': 0,
                    'name': 'Point1',
                    'color': '#00FF00'
                },
                {
                    'x': 1,
                    'y': 5,
                    'name': 'Point2',
                    'color': '#CCC'
                },
                {
                    'x': 2,
                    'y': 3,
                    'name': 'Point3',
                    'color': '#999'
                },
                {
                    'x': 3,
                    'y': 5,
                    'name': 'Point4',
                    'color': '#000'
                }
              ]

          :param value: The value that should contain the data which will be converted into data
            point instances.

            .. note::

              If ``value`` is not an iterable, it will be converted into an iterable to be
              further de-serialized correctly.

          :type value: iterable

          :returns: Collection of :term:`data point` instances (descended from
            :class:`DataBase <highcharts_maps.options.series.data.base.DataBase>`)
          :rtype: :class:`list <python:list>` of
            :class:`DataBase <highcharts_maps.options.series.data.base.DataBase>`-descendant
            instances

  .. tab:: Load to Existing Series

    .. tabs::

      .. tab:: Using ``.load_from_csv()``

        .. include:: using/populating_series_data/_load_from_csv.rst

      .. tab:: Using ``.load_from_pandas()``

        .. include:: using/populating_series_data/_load_from_pandas.rst

      .. tab:: Using ``.load_from_geopandas()``

        .. include:: using/populating_series_data/_load_from_geopandas.rst

      .. tab:: Using ``.load_from_pyspark()``

        .. include:: using/populating_series_data/_load_from_pyspark.rst


  .. tab:: Create a New Series

    .. tabs::

      .. tab:: Using ``.from_csv()``

        .. include:: using/populating_series_data/_new_from_csv.rst

      .. tab:: Using ``.from_pandas()``

        .. include:: using/populating_series_data/_new_from_pandas.rst

      .. tab:: Using ``.from_geopandas()``

        .. include:: using/populating_series_data/_new_from_geopandas.rst

      .. tab:: Using ``.from_pyspark()``

        .. include:: using/populating_series_data/_new_from_pyspark.rst

.. _adding_series_to_charts:

Adding Series to Charts
=============================

Now that you have constructed your :term:`series` instances, you can add them to
:term:`charts` very easily. First, **Highcharts for Python** represents visualizations as
instances of the :class:`Chart <highcharts_maps.chart.Chart>` class. This class contains
an :meth:`options <highcharts_maps.chart.Chart.options>` property, which itself contains
an instance of
:class:`HighchartsMapsOptions <highcharts_maps.options.HighchartsMapsOptions>`.

  .. note::

    The :class:`HighchartsMapsOptions <highcharts_maps.options.HighchartsMapsOptions>`
    is a sub-class of the **Highcharts for Python**
    :class:`HighchartsOptions <highcharts_maps.options.HighchartsOptions>` class, and is
    fully backwards-compatible with it. This means that you can use them interchangeably
    when using **Highcharts Maps for Python**, as the
    :class:`HighchartsMapsOptions <highcharts_maps.options.HighchartsMapsOptions>`
    class merely extends its parent with a number of methods and properties that are
    specifically supported by
    `Highcharts Maps <https://www.highcharts.com/products/maps/>`__.

  .. note::

    This structure - where the chart object contains an options object - is a little
    nested for some tastes, but it is the structure which
    `Highcharts (JS) <https://www.highcharts.com>`__ has adopted and
    so for the sake of consistency the **Highcharts for Python Toolkit** uses it as well.

To be visualized on your chart, you will need to add your series instances to the
:meth:`Chart.options.series <highcharts_maps.options.HighchartsOptions.series>`
property. You can do this in several ways:

.. tabs::

  .. tab:: Using ``.options.series``

    .. include:: using/assembling_your_chart/_using_series_property.rst

  .. tab:: Using ``.add_series()``

    .. include:: using/assembling_your_chart/_using_add_series.rst

  .. tab:: Using ``.from_series()``

    .. include:: using/assembling_your_chart/_using_from_series.rst

  .. tab:: Using ``.from_geopandas()``

    .. include:: using/assembling_your_chart/_using_from_geopandas.rst

--------------------

**************************************
Rendering Your Visualizations
**************************************

Once you have created your :class:`Chart <highcharts_maps.chart.Chart>` instance or
instances, you can render them very easily. There are really only two ways to display
your visualizations:

  #. :ref:`Render Visualizations in Web Content <web_rendering>`
  #. :ref:`Render Visualizations in Jupyter Labs / Jupyter Notebook <jupyter_rendering>`

.. _web_rendering:

Rendering Highcharts Visualizations in Web Content
========================================================

`Highcharts <https://www.highcharts.com>`__ is a suite of JavaScript libraries 
designed to enable rendering high-end data visualizations in a web context. They are 
designed and optimized to operate within a web browser. The 
**Highcharts for Python Toolkit** therefore fully supports this capability, and we've 
enabled it using the *batteries included* principle.

To render a **Highcharts Maps for Python** visualization, all you need is for the browser
to execute the output of the chart's
:meth:`.to_js_literal() <highcharts_maps.chart.Chart.to_js_literal>` method, which will
return a snippet of JavaScript code which when included in a web page will display the
chart in full.

.. warning::

  The current version of **Highcharts Maps for Python** assumes that your web content
  already has all the ``<script/>`` tags which include the
  `Highcharts Core <https://www.highcharts.com/products/highcharts>`__ and
  `Highcharts Maps <https://www.highcharts.com/products/maps/>`__ modules your chart
  relies on.

  This is likely to change in a future version of **Highcharts for Python**, where the
  toolkit will support the production of ``<script/>`` tags (see roadmap :issue:`6`).

For example:

.. include:: using/rendering_your_visualizations/_as_web_content.rst

Now you can use whatever front-end framework you are using to insert that string into your
application's HTML output (in an appropriate ``<script/>`` tag, of course).

.. tip::

  The same principle applies to the use of
  :class:`SharedMapsOptions <highcharts_maps.global_options.shared_options.SharedMapsOptions>`.

  It is recommended to place the JS literal form of your shared options *before* any of
  the charts that you will be visualizing.

  .. seealso::

    * :ref:`Organizing Your Highcharts for Python Project > Use Shared Options <shared_options>`

.. _jupyter_rendering:

Rendering Highcharts for Python in Jupyter Labs or Jupyter Notebooks
======================================================================

You can also render **Highcharts Maps for Python** visualizations inside your
`Jupyter <https://jupyter.org/>`_ notebook. This is as simple as executing a single
:meth:`.display() <highcharts_maps.chart.Chart.display>` call on your
:class:`Chart <highcharts_maps.chart.Chart>` instance:

.. include:: using/rendering_your_visualizations/_as_jupyter.rst

|

You can call the :meth:`.display() <highcharts_maps.chart.Chart.display>` method 
from anywhere within any notebook cell, and it will render the resulting chart in your 
notebook's output. That's it!

  .. caution::

    If `iPython <https://ipython.readthedocs.io/>`_ is not available in your runtime
    environment, calling
    :meth:`.display() <highcharts_maps.chart.Chart.display>` will raise a
    :exc:`HighchartsDependencyError`.

Maps Chart vs Regular Chart
==================================

When using **Highcharts Maps for Python** you have the choice to render your charts
using the `Highcharts Maps <https://www.highcharts.com/products/maps/>`__ chart
constructor or the standard
`Highcharts Core <https://www.highcharts.com/products/highcharts/>`__ chart constructor.

The difference between these two constructors relates to the features available in the
chart. The Highcharts Maps chart will be visualized including a map (configured in
:meth:`Chart.options.chart.map <highcharts_maps.options.chart.ChartOptions.map>`,
:meth:`Chart.options.map_view <highcharts_maps.options.HighchartsMapsOptions.map_view>`,
and
:meth:`Chart.options.map_navigation <highcharts_maps.options.HighchartsMapsOptions.map_navigation>`).
A regular Highcharts JS chart cannot be displayed with either of these elements.

However, Highcharts Maps *can* visualize all of the series types offered by
`Highcharts Core <https://www.highcharts.com/products/highcharts/>`__.

When working with your :class:`Chart <highcharts_maps.chart.Chart>` object, you can set
the :meth:`.is_maps_chart <highcharts_maps.chart.Chart.is_maps_chart>` property to
``True`` to force the chart to be rendered using the (JavaScript)
``Highcharts.mapChart()`` constructor.

If you wish to force the use of the (JavaScript) ``Highcharts.chart()``
constructor, you can explicitly set
:meth:`.is_maps_chart <highcharts_maps.chart.Chart.is_maps_chart>` to ``False`` after
populating the chart's :meth:`.options <highcharts_maps.chart.Chart.options>` property.

If you do not set this property explicitly, **Highcharts Maps for Python** will make
a determination based on the contents of the
:meth:`.options <highcharts_maps.chart.Chart.options>` property. If that that property
is set to a
:class:`HighchartsMapsOptions <highcharts_maps.options.HighchartsMapsOptions>`
instance, the :meth:`.is_maps_chart <highcharts_maps.chart.Chart.is_maps_chart>`
property will be set to ``True``, unless explicitly overridden in your code.

---------------------------

.. sidebar:: Highcharts Export Server

  Highsoft - the developers of `Highcharts (JS) <https://www.highcharts.com>`__ - 
  provide a rate-limited publicly available :term:`Export Server` that can be
  used by `Highcharts <https://www.highcharts.com>`__ license-holders. By default,
  the **Highcharts for Python Toolkit** is configured to use this server.

  However, there are many use cases where you may be deploying your own
  :term:`Export Server` and wish to use that instead. You can do this by
  creating your own
  :class:`ExportServer <highcharts_stock.headless_export.ExportServer>` instance and
  supplying it as the ``server_instance`` keyword argument to the ``.download_chart()``
  method.

********************************************
Downloading Your Visualizations
********************************************

Sometimes you are not looking to produce an interactive web-based visualization of your
data, but instead are looking to produce a static image of your visualization that can
be downloaded, emailed, or embedded in some other documents.

With **Highcharts Maps for Python**, that's as simple as executing the
:meth:`Chart.download_chart() <highcharts_maps.chart.Chart.download_chart>` method.

When you have defined a :class:`Chart <highcharts_maps.chart.Chart>` instance, you can
download a static version of that chart or persist it to a file in your runtime
environment. The actual file itself is produced using a
:term:`Highcharts Export Server <Export Server>`.

|

|

.. tabs::

  .. tab:: Using Highsoft's Export Server

    .. include:: using/download_visualizations/_using_highsoft.rst

  .. tab:: Using a Custom Server

    .. include:: using/download_visualizations/_using_custom.rst

.. warning::

  As of Highcharts for Python v.1.1.0, the Highcharts :term:`Export Server` does not yet fully 
  support all of the series types added in Highcharts (JS) v.11. Attempting to programmatically download
  one of those new as-yet-unsupported visualizations will generate a 
  :exc:`HighchartsUnsupportedExportError <highcharts_maps.errors.HighchartsUnsupportedExportError>`.

-----------------------------

.. _custom_projections:

*********************************
Using Custom Projections
*********************************

All maps are :term:`projections <projection>` of a three-dimensional globe onto a
two-dimensional plane (a map). Any such projection will in some ways distort the
proportions of the areas depicted, and you may want to apply a different projection
to better communicate insights from your data.

Projections are configured using the
:meth:`MapViewOptions.projection <highcharts_maps.options.map_views.MapViewOptions.projection>`
property, which takes a
:class:`ProjectionOptions <highcharts_maps.utility_classes.projections.ProjectionOptions>`
instance. You can define a custom projection algorithm to apply using the
:meth:`ProjectionOptions.custom <highcharts_maps.utility_classes.projections.ProjectionOptions.custom>`
property, which takes a
:class:`CustomProjection <highcharts_maps.utility_classes.projections.CustomProjection>`
instance.

A :class:`CustomProjection <highcharts_maps.utility_classes.projections.CustomProjection>`
is a :class:`JavaScriptClass <highcharts_maps.utility_classes.javascript_functions.JavaScriptClass>`
which is used to calculate your map projection to/from a given set of latitude and
longitude coordinates. In order to be valid, it needs to:

  * be given a :meth:`.name <highcharts_maps.utility_classes.projections.CustomProjection.name>`
  * have a ``constructor`` method which sets a (JavaScript) ``this.projection`` property
    as a JavaScript function or class
  * have a ``forward`` method which accepts a longitude and latitude array (2-member
    array of longitude and latitude coordinates, respectively)
  * have an ``inverse`` method which accepts a point array (2-member array of projected
    horizontal and vertical coordinates, respectively)

An example of how this might be represented, using (JavaScript) ``d3-geo`` to create a
"Robinson" projection would be:

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - Python
    - JavaScript
  * - .. code-block:: python

        from highcharts_maps.utility_classes.projections import CustomProjection
        from highcharts_maps.utility_classes.javascript_functions import CallbackFunction

        robinson_constructor = CallbackFunction(
            function_name = 'constructor',
            arguments = None,
            body = """this.projection = window.d3.geoRobinson().reflectY(true);"""
        )

        robinson_forward = CallbackFunction(
            function_name = 'forward',
            arguments = ['lonLat'],
            body = """return this.projection(lonLat);"""
        )

        robinson_inverse = CallbackFunction(
            function_name = 'inverse',
            arguments = ['point'],
            body = """return this.projection.invert(point);"""
        )

        robinson_projection = CustomProjection(
            class_name = 'RobinsonProjectionDefinition',
            name = 'Robinson',
            methods = [
                robinson_constructor,
                robinson_forward,
                robinson_inverse
            ]
        )

        my_chart.set_custom_projection(robinson_projection)

    - .. code-block:: javascript

        class RobinsonProjectionDefinition {
          constructor() {
            this.projection = window.d3.geoRobinson().reflectY(true);
          }

          forward(lonLat) {
            return this.projection(lonLat);
          }

          inverse(point) {
            return this.projection.invert(point);
          }
        }
        Highcharts.Projection.add('Robinson', RobinsonProjectionDefinition);

        Highcharts.mapChart('container', {

          // .. OTHER PROPERTIES GO HERE ...

          mapView: {
            projection: {
              name: 'Robinson',
            },
            // .. OTHER PROPERTIES GO HERE ...
          },

          // .. OTHER PROPERTIES GO HERE ...
        });


.. warning::

  You may rely on outside libraries (like ``d3-geo``) to compute your custom projections.
  Be careful to make sure they are imported using appropriate ``<script/>`` tags and
  initialized appropriately in your client-side JavaScript. **Highcharts Maps for Python**
  provides *no* introspection of your JavaScript code, so you will have to make sure
  you've laid appropriate groundwork in the code into which you will be inserting your
  **Highcharts Maps for Python** serialized JavaScript.

Once you have defined your
:class:`CustomProjection <highcharts_maps.utility_classes.projections.CustomProjection>`,
you can apply it to your chart either using the
:meth:`Chart.set_custom_projection() <highcharts_maps.chart.Chart.set_custom_projection>`
convenience method or by setting
:meth:`Chart.options.map_view.custom <highcharts_maps.options.map_views.MapViewOptions.custom>`
directly.

------------------------------

.. target-notes::

.. include:: links.txt

.. _`Jupyter Notebook`: https://jupyter.org
.. _`Jupyter Labs`: https://jupyter.org
.. _IPython: https://ipython.readthedocs.io/
.. _pandas: https://pandas.pydata.org
.. _PySpark: https://spark.apache.org/docs/latest/api/python/
.. _geopandas: https://geopandas.org/