
The structure of the **Highcharts Maps for Python** library closely matches the structure
of the `Highcharts Maps <https://www.highcharts.com/products/maps/>`__ options object (see the relevant
`reference documentation <https://api.highcharts.com/highmaps/>`_).

At the root of the library - importable from ``highcharts_maps`` - you will find the
:mod:`highcharts_maps.highcharts` module. This module is a catch-all importable module,
which allows you to easily access the most-commonly-used Highcharts Maps for Python
classes and modules.

.. note::

  Whlie you can access all of the **Highcharts Maps for Python** classes from
  ``highcharts_maps.highcharts``, if you want to more precisely navigate to specific
  class definitions you can do fairly easily using the module organization and naming
  conventions used in the library.

  *This is the recommended best practice to maximize performance*.

  In the root of the ``highcharts_maps`` library you can find universally-shared
  class definitions, like :mod:`.metaclasses <highcharts_maps.metaclasses>` which
  contains the :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>`
  and :class:`JavaScriptDict <highcharts_maps.metaclasses.JavaScriptDict>`
  definitions, or :mod:`.decorators <highcharts_maps.decorators>` which define
  method/property decorators that are used throughout the library.

  The :mod:`.utility_classes <highcharts_maps.utility_classes>` module contains class
  definitions for classes that are referenced or used throughout the other class
  definitions.

  And you can find the Highcharts Maps ``options`` object and all of its
  properties defined in the :mod:`.options <highcharts_maps.options>` module, with
  specific (complicated or extensive) sub-modules providing property-specific classes
  (e.g. the :mod:`.options.plot_options <highcharts_maps.options.plot_options>`
  module defines all of the different configuration options for different series types,
  while the :mod:`.options.series <highcharts_maps.options.series>` module defines all
  of the classes that represent :term:`series` of data in a given chart).
