from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_maps.decorators import class_sensitive
from highcharts_maps.options.plot_options.base import MapBaseOptions
from highcharts_maps.options.plot_options.generic import GenericTypeOptions
from highcharts_core.options.plot_options.drag_drop import DragDropOptions
from highcharts_maps.utility_functions import validate_color, mro__to_untrimmed_dict
from highcharts_maps.utility_classes.gradients import Gradient
from highcharts_maps.utility_classes.patterns import Pattern
from highcharts_maps.utility_classes.clusters import ClusterOptions


class MapPointOptions(MapBaseOptions, GenericTypeOptions):
    """Map Points are a special version of a scatter series where the points are
    positioned according to geographic coordinates within a map.

    .. figure:: ../../../_static/mappoint-example.png
      :alt: Map Point Example chart
      :align: center

    .. tip::

      **Best practice!**

      This can be very useful for rendering cities or other locations on your map.

    """

    def __init__(self, **kwargs):
        self._animation_limit = None
        self._boost_blending = None
        self._boost_threshold = None
        self._color_axis = None
        self._color_index = None
        self._color_key = None
        self._cluster = None
        self._data_as_columns = None
        self._drag_drop = None
        self._find_nearest_point_by = None
        self._negative_color = None

        self.animation_limit = kwargs.get('animation_limit', None)
        self.boost_blending = kwargs.get('boost_blending', None)
        self.boost_threshold = kwargs.get('boost_threshold', None)
        self.color_axis = kwargs.get('color_axis', None)
        self.color_index = kwargs.get('color_index', None)
        self.color_key = kwargs.get('color_key', None)
        self.cluster = kwargs.get('cluster', None)
        self.data_as_columns = kwargs.get('data_as_columns', None)
        self.drag_drop = kwargs.get('drag_drop', None)
        self.find_nearest_point_by = kwargs.get('find_nearest_point_by', None)
        self.negative_color = kwargs.get('negative_color', None)

        super().__init__(**kwargs)

    @property
    def animation_limit(self) -> Optional[int | float | Decimal]:
        """For some series, there is a limit that shuts down initial animation by default
        when the total number of points in the chart is too high. Defaults to
        :obj:`None <python:None>`.

        For example, for a column chart and its derivatives, animation does not run if
        there is more than 250 points totally. To disable this cap, set
        ``animation_limit`` to ``float("inf")`` (which represents infinity).

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._animation_limit

    @animation_limit.setter
    def animation_limit(self, value):
        if value == float('inf'):
            self._animation_limit = float('inf')
        else:
            self._animation_limit = validators.numeric(value,
                                                       allow_empty = True,
                                                       minimum = 0)

    @property
    def boost_blending(self) -> Optional[str]:
        """Sets the color blending in the boost module. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._boost_blending

    @boost_blending.setter
    def boost_blending(self, value):
        self._boost_blending = validators.string(value, allow_empty = True)

    @property
    def boost_threshold(self) -> Optional[int]:
        """Set the point threshold for when a series should enter boost mode. Defaults to
        ``5000``.

        Setting it to e.g. 2000 will cause the series to enter boost mode when there are
        2,000 or more points in the series.

        To disable boosting on the series, set the ``boost_threshold`` to ``0``. Setting
        it to ``1`` will force boosting.

        .. note::

          The :meth:`AreaOptions.crop_threshold` also affects this setting.

          When zooming in on a series that has fewer points than the ``crop_threshold``,
          all points are rendered although outside the visible plot area, and the
          ``boost_threshold`` won't take effect.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._boost_threshold

    @boost_threshold.setter
    def boost_threshold(self, value):
        self._boost_threshold = validators.integer(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def color_axis(self) -> Optional[str | int | bool]:
        """When using dual or multiple color axes, this setting defines which
        :term:`color axis` the particular series is connected to. It refers to either the
        :meth:`ColorAxis.id` or the index of the axis in the :class:`ColorAxis` array,
        with ``0`` being the first. Set this option to ``False`` to prevent a series from
        connecting to the default color axis.

        Defaults to ``0``.

        :rtype: :obj:`None <python:None>` or :class:`str <python:str>` or
          :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._color_axis

    @color_axis.setter
    def color_axis(self, value):
        if value is None:
            self._color_axis = None
        elif value is False:
            self._color_axis = False
        else:
            try:
                self._color_axis = validators.string(value)
            except TypeError:
                self._color_axis = validators.integer(value,
                                                      minimum = 0)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def color_key(self) -> Optional[str]:
        """Determines what data value should be used to calculate point color if
        :meth:`AreaOptions.color_axis` is used.

        .. note::

          Requires to set ``min`` and ``max`` if some custom point property is used or if
          approximation for data grouping is set to ``'sum'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color_key

    @color_key.setter
    def color_key(self, value):
        self._color_key = validators.string(value, allow_empty = True)

    @property
    def cluster(self) -> Optional[ClusterOptions]:
        """Options for marker clusters, the concept of sampling the data values into
        larger blocks in order to ease readability and increase performance of the
        JavaScript charts.

        .. warning::

          The marker clusters module does not work with ``boost`` and ``draggable-points``
          modules.

        .. note::

          The marker clusters feature requires the ``marker-clusters.js`` file to be
          loaded, found in the modules directory of the download package, or online at
          `code.highcharts.com/modules/marker-clusters.js <code.highcharts.com/modules/marker-clusters.js>`_.

        :rtype: :class:`ClusterOptions` or :obj:`None <python:None>`
        """
        return self._cluster

    @cluster.setter
    @class_sensitive(ClusterOptions)
    def cluster(self, value):
        self._cluster = value

    @property
    def data_as_columns(self) -> Optional[bool]:
        """If ``True``, indicates that the data is structured as columns instead of as
        rows. Defaults to :obj:`None <python:None>`, which behaves as ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._data_as_columns

    @data_as_columns.setter
    def data_as_columns(self, value):
        if value is None:
            self._data_as_columns = None
        else:
            self._data_as_columns = bool(value)

    @property
    def drag_drop(self) -> Optional[DragDropOptions]:
        """The draggable-points module allows points to be moved around or modified in the
        chart.

        In addition to the options mentioned under the dragDrop API structure, the module
        fires three (JavaScript) events:

          * ``point.dragStart``
          * ``point.drag``
          * ``point.drop``

        :rtype: :class:`DragDropOptions` or :obj:`None <python:None>`
        """
        return self._drag_drop

    @drag_drop.setter
    @class_sensitive(DragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def find_nearest_point_by(self) -> Optional[str]:
        """Determines whether the series should look for the nearest point in both
        dimensions or just the x-dimension when hovering the series.

        If :obj:`None <python:None>`, defaults to ``'xy'`` for scatter series and ``'x'``
        for most other series. If the data has duplicate x-values, it is recommended to
        set this to ``'xy'`` to allow hovering over all points.

        Applies only to series types using nearest neighbor search (not direct hover) for
        tooltip.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._find_nearest_point_by

    @find_nearest_point_by.setter
    def find_nearest_point_by(self, value):
        self._find_nearest_point_by = validators.string(value, allow_empty = True)

    @property
    def negative_color(self) -> Optional[str | Gradient | Pattern]:
        """The color for the parts of the graph or points that are below the
        :meth:`AreaOptions.threshold`.

        .. note::

          :meth:`Zones <AreaOptions.zones>` take precedence over the negative color.
          Using ``negative_color`` is equivalent to applying a zone with value of 0.

        :rtype: :class:`str <python:str>` or
          :class:`Gradient <highcharts_maps.utility_classes.gradients.Gradient>` or
          :class:`Pattern <highcharts_maps.utility_classes.patterns.Pattern>` or
          :obj:`None <python:None>`
        """
        return self._negative_color

    @negative_color.setter
    def negative_color(self, value):
        self._negative_color = validate_color(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'negative_color': as_dict.get('negativeColor', None),

            'all_areas': as_dict.get('allAreas', None),
            'join_by': as_dict.get('joinBy', None),

            'cluster': as_dict.get('cluster', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'animationLimit': self.animation_limit,
            'boostBlending': self.boost_blending,
            'boostThreshold': self.boost_threshold,
            'colorAxis': self.color_axis,
            'colorIndex': self.color_index,
            'colorKey': self.color_key,
            'cluster': self.cluster,
            'dataAsColumns': self.data_as_columns,
            'dragDrop': self.drag_drop,
            'findNearestPointBy': self.find_nearest_point_by,
            'negativeColor': self.negative_color,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
