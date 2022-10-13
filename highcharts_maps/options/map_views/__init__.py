from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_maps import errors
from highcharts_maps.decorators import class_sensitive
from highcharts_maps.metaclasses import HighchartsMeta
from highcharts_maps.utility_functions import validate_bounding_array

from highcharts_maps.options.map_views.insets import (InsetOptions, Inset)
from highcharts_maps.utility_classes.projections import ProjectionOptions


class MapViewOptions(HighchartsMeta):
    """Configuration options for the initial view of a map visualization and for the
    :term:`projection` to be applied to the map."""

    def __init__(self, **kwargs):
        self._center = None
        self._inset_options = None
        self._insets = None
        self._max_zoom = None
        self._padding = None
        self._projection = None
        self._zoom = None

        self.center = kwargs.get('center', None)
        self.inset_options = kwargs.get('inset_options', None)
        self.insets = kwargs.get('insets', None)
        self.max_zoom = kwargs.get('max_zoom', None)
        self.padding = kwargs.get('padding', None)
        self.projection = kwargs.get('projection', None)
        self.zoom = kwargs.get('zoom', None)

    @property
    def center(self) -> Optional[List[int | float | Decimal]]:
        """The center of the map, expressed as longitude and latitude values. Defaults to
        ``[0, 0]``.

        .. note::

          For preprojected maps (like the GeoJSON files in Map Collection v1.x), the units
          are projected x and y units.

        :rtype: 2-member :class:`list <python:list>` of numeric values, or
          :obj:`None <python:None>`
        """
        return self._center

    @center.setter
    def center(self, value):
        if not value:
            self._center = None
        else:
            value = validators.iterable(value)
            if not len(value) == 2:
                raise errors.HighchartsValueError(f'center expects a 2-member iterable or'
                                                  f'None. Received a {len(value)}-member '
                                                  f'iterable.')
            self._center = [validators.numeric(x) for x in value]

    @property
    def inset_options(self) -> Optional[InsetOptions]:
        """Generic configuration settings for the placement and appearance of map insets,
        such as those used for non-contiguous territories.

        :rtype: :class:`InsetOptions <highcharts_maps.options.map_views.insets.InsetOptions>`
          or :obj:`None <python:None>`
        """
        return self._inset_options

    @inset_options.setter
    @class_sensitive(InsetOptions)
    def inset_options(self, value):
        self._inset_options = value

    @property
    def insets(self) -> Optional[List[Inset]]:
        """Definition of the :term:`insets <map inset>` to be rendered, typically used
        for a non-contiguous territory. Each inset included inherits properties from
        :meth:`.inset_options <highcharts_maps.options.map_views.MapViewOptions.inset_options>`
        which can be overridden. Defaults to :obj:`None <python:None>`.

        .. note::

          Some of the :term:`TopoJSON` files contained in the
          :term:`Highcharts Maps Collection` include a property called
          ``hc-recommended-mapview``, some of which include insets. To override these
          inset configurations, supply an inset with a matching
          :meth:`.id <highcharts_maps.options.map_views.insets.Inset.id>`.
          The inset supplied will take precedence.

        :rtype: :class:`list <python:list>` of
          :class:`Inset <highcharts_maps.options.map_views.insets.Inset>`
          instances, or :obj:`None <python:None>`
        """
        return self._insets

    @insets.setter
    @class_sensitive(Inset, force_iterable = True)
    def insets(self, value):
        self._insets = value

    @property
    def max_zoom(self) -> Optional[int | float | Decimal]:
        """The maximum zoom level beyond which the user cannot zoom. Defaults to
        :obj:`None <python:None>`.

          .. seealso::

            * :meth:`MapViewOptions.zoom <highcharts_maps.options.map_views.MapViewOptions.zoom>`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_zoom

    @max_zoom.setter
    def max_zoom(self, value):
        self._max_zoom = validators.numeric(value,
                                            allow_empty = True,
                                            minimum = 0)

    @property
    def padding(self) -> Optional[str | int | float | Decimal | List[str | int | float | Decimal]]:
        """The padding inside the plot area when auto fitting to the map bounds. Defaults
        to ``0``.

        Accepts:

          * a number, representing pixels
          * a percentage string, relative to the plot area
          * an array of numbers or percentage strings, corresponding to top, right,
            bottom, and left respectively

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`,
          4-member :class:`list <python:list>` of :class:`str <python:str>` or
          :class:`int <python:int>`, or :obj:`None <python:None>`
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = validate_bounding_array(value)

    @property
    def projection(self) -> Optional[ProjectionOptions]:
        """The projection options allow applying client side projection to a map given in
        geographic coordinates, typically from :term:`TopoJSON` or :term:`GeoJSON`.

        :rtype: :class:`ProjectionOptions <highcharts_maps.utility_classes.projections.ProjectionOptions>`
          or :obj:`None <python:None>`
        """
        return self._projection

    @projection.setter
    @class_sensitive(ProjectionOptions)
    def projection(self, value):
        self._projection = value

    @property
    def zoom(self) -> Optional[int | float | Decimal]:
        """The zoom level to apply to the map. Higher zoom levels mean more zoomed in. An
        increase of 1 zooms in to a quarter of the viewed area (half the width and height).
        If :obj:`None <python:None>`, defaults to fitting to the map bounds. Defaults to
        :obj:`None <python:None>`.

        .. note::

          In a ``WebMercator`` projection, a zoom level of ``0`` represents the world in a
          256x256 pixel square. This is a common concept for WMS tiling software.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._zoom

    @zoom.setter
    def zoom(self, value):
        self._zoom = validators.numeric(value, allow_empty = True, minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'center': as_dict.get('center', None),
            'inset_options': as_dict.get('insetOptions', None),
            'insets': as_dict.get('insets', None),
            'max_zoom': as_dict.get('maxZoom', None),
            'padding': as_dict.get('padding', None),
            'projection': as_dict.get('projection', None),
            'zoom': as_dict.get('zoom', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'center': self.center,
            'insetOptions': self.inset_options,
            'insets': self.insets,
            'maxZoom': self.max_zoom,
            'padding': self.padding,
            'projection': self.projection,
            'zoom': self.zoom,
        }

        return untrimmed
