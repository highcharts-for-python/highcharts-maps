"""Implements the :class:`HighchartsOptions` class."""
from typing import Optional, List

from validator_collection import validators

from highcharts_maps.decorators import class_sensitive
from highcharts_maps.options.series.series_generator import create_series_obj

from highcharts_maps.options.chart import ChartOptions
from highcharts_maps.global_options.language import Language
from highcharts_maps.options.navigation import Navigation
from highcharts_maps.options.plot_options import PlotOptions
from highcharts_maps.options.plot_options.generic import GenericTypeOptions

# Highcharts Maps Classes
from highcharts_maps.options.map_navigation import MapNavigationOptions
from highcharts_maps.options.map_views import MapViewOptions

from highcharts_core.options import Options, HighchartsOptions


class HighchartsMapsOptions(HighchartsOptions):
    """The Python representation of the
    `Highcharts Stock <https://api.highcharts.com/highstock/>`_ configuration object."""

    def __init__(self, **kwargs):
        self._map_navigation = None
        self._map_view = None

        self.map_navigation = kwargs.get('map_navigation', None)
        self.map_view = kwargs.get('map_view', None)

        super().__init__(**kwargs)

    @property
    def chart(self) -> Optional[ChartOptions]:
        """General options for the chart.

        .. note::

          This property is perhaps one of the most important properties you will use when
          configuring your Highcharts data visualization.

        :returns: A :class:`ChartOptions` configuration object or
          :obj:`None <python:None>`
        :rtype: :class:`ChartOptions` or :obj:`None <python:None>`
        """
        return self._chart

    @chart.setter
    @class_sensitive(ChartOptions)
    def chart(self, value):
        self._chart = value

    @property
    def language(self) -> Optional[Language]:
        """Language object which can be used to configure the specific text to use in the
        chart.

        .. note::

          When working in JavaScript, the ``lang`` configuration is global and it can't be
          set on each chart initialization.

          Instead, use ``Highcharts.setOptions()`` to set it before any chart is
          initialized.

        :returns: A :class:`Language` object or :obj:`None <python:None>`
        :rtype: :class:`Language` or :obj:`None <python:None>`
        """
        return self._language

    @language.setter
    @class_sensitive(Language)
    def language(self, value):
        self._language = value

    @property
    def map_navigation(self) -> Optional[MapNavigationOptions]:
        """Configuration options for the buttons that handle navigation and zooming within
        map visualizations.

        :rtype: :class:`MapNavigationOptions <highcharts_maps.options.map_navigation.MapNavigationOptions>`
          or :obj:`None <python:None>`
        """
        return self._map_navigation

    @map_navigation.setter
    @class_sensitive(MapNavigationOptions)
    def map_navigation(self, value):
        self._map_navigation = value

    @property
    def map_view(self) -> Optional[MapViewOptions]:
        """Configuration options for the initial view of a map visualization and for the
        :term:`projection` to be applied to the map.

        :rtype: :class:`MapViewOptions <highcharts_maps.options.map_view.MapViewOptions>`
          or :obj:`None <python:None>`
        """
        return self._map_view

    @map_view.setter
    @class_sensitive(MapViewOptions)
    def map_view(self, value):
        self._map_view = value

    @property
    def navigation(self) -> Optional[Navigation]:
        """A collection of options for buttons and menus appearing in the exporting
        module or in Stock Tools.

        :returns: The configuration of the navigation buttons.
        :rtype: ;class:`Navigation` or :obj:`None <python:None>`
        """
        return self._navigation

    @navigation.setter
    @class_sensitive(Navigation)
    def navigation(self, value):
        self._navigation = value

    @property
    def plot_options(self) -> Optional[PlotOptions]:
        """A wrapper object for configurations applied to each series type.

        The config objects for each series can also be overridden for each series item as
        given in the series array.

        Configuration options for the series are given in three levels:

          * Options for all series in a chart are given in the
            :meth:`series <PlotOptions.series>` property.
          * Options for all series of a specific type are given in the corresponding
            property for that type, for example
            :meth:`plot_options.line <PlotOptions.line>`.
          * Finally, options for one single series are given in the
            :meth:`series <Options.series>` array.

        :returns: Configurations for how series should be plotted / displayed.
        :rtype: :class:`PlotOptions` or :obj:`None <python:None>`
        """
        return self._plot_options

    @plot_options.setter
    @class_sensitive(PlotOptions)
    def plot_options(self, value):
        self._plot_options = value

    @property
    def series(self) -> Optional[List[GenericTypeOptions]]:
        """Series options for specific data and the data itself.

        :returns: The series to display along with configuration and data.
        :rtype: :class:`Series` or :obj:`None <python:None>`
        """
        return self._series

    @series.setter
    def series(self, value):
        value = validators.iterable(value, allow_empty = True)
        default_series_type = None
        if self.chart:
            default_series_type = self.chart.type
        if not value:
            self._series = None
        else:
            self._series = [create_series_obj(x,
                                              default_type = default_series_type)
                            for x in value]

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        as_dict = validators.dict(as_dict, allow_empty = True) or {}

        kwargs_dict = {
            'accessibility': as_dict.get('accessibility', None),
            'annotations': as_dict.get('annotations', None),
            'caption': as_dict.get('caption', None),
            'chart': as_dict.get('chart', None),
            'color_axis': as_dict.get('colorAxis', None),
            'colors': as_dict.get('colors', None),
            'credits': as_dict.get('credits', None),
            'data': as_dict.get('data', None),
            'defs': as_dict.get('defs', None),
            'drilldown': as_dict.get('drilldown', None),
            'exporting': as_dict.get('exporting', None),
            'language': as_dict.get('lang', None),
            'legend': as_dict.get('legend', None),
            'loading': as_dict.get('loading', None),
            'navigation': as_dict.get('navigation', None),
            'plot_options': as_dict.get('plotOptions', None),
            'responsive': as_dict.get('responsive', None),
            'series': as_dict.get('series', None),
            'sonification': as_dict.get('sonification', None),
            'subtitle': as_dict.get('subtitle', None),
            'time': as_dict.get('time', None),
            'title': as_dict.get('title', None),
            'tooltip': as_dict.get('tooltip', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_axis': as_dict.get('zAxis', None),

            'map_navigation': as_dict.get('mapNavigation', None),
            'map_view': as_dict.get('mapView', None),
        }

        return kwargs_dict

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'annotations': self.annotations,
            'caption': self.caption,
            'chart': self.chart,
            'colorAxis': self.color_axis,
            'colors': self.colors,
            'credits': self.credits,
            'data': self.data,
            'defs': self.defs,
            'drilldown': self.drilldown,
            'exporting': self.exporting,
            'lang': self.language,
            'legend': self.legend,
            'loading': self.loading,
            'mapNavigation': self.map_navigation,
            'mapView': self.map_view,
            'navigation': self.navigation,
            'plotOptions': self.plot_options,
            'responsive': self.responsive,
            'series': self.series,
            'sonification': self.sonification,
            'subtitle': self.subtitle,
            'time': self.time,
            'title': self.title,
            'tooltip': self.tooltip,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
            'zAxis': self.z_axis,
        }

        return untrimmed
