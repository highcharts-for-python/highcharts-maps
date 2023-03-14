from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_maps import errors
from highcharts_maps.decorators import class_sensitive
from highcharts_maps.metaclasses import HighchartsMeta
from highcharts_maps.utility_classes.gradients import Gradient
from highcharts_maps.utility_classes.patterns import Pattern
from highcharts_maps.utility_classes.projections import ProjectionOptions
from highcharts_maps.utility_classes.geojson import MultiLineString, Polygon
from highcharts_maps.utility_functions import validate_color, validate_bounding_array


class InsetOptions(HighchartsMeta):
    """Generic configuration settings for the placement and appearance of
    :term:`map insets <map inset>`, such as those used for non-contiguous territories."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._padding = None
        self._relative_to = None
        self._units = None

        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.padding = kwargs.get('padding', None)
        self.relative_to = kwargs.get('relative_to', None)
        self.units = kwargs.get('units', None)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The border color drawn around the inset. Defaults to
        ``'#cccccc'``.

        :returns: The color of the inset border.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = validate_color(value)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The border width (in pixels) applied to the inset border. Defaults to
        ``1``.

        :returns: The border width to apply to the inset border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def padding(self) -> Optional[str | int | float | Decimal | List[str | int | float | Decimal]]:
        """The padding of the insets. Defaults to ``'10%'``.

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
    def relative_to(self) -> Optional[str]:
        """The coordinate system that the inset's
        :meth:`.field <highcharts_maps.options.map_views.insets.Inset.field>` and
        :meth:`.border_path <highcharts_maps.options.map_views.insets.Inset.border_path>`
        should relate to. Defaults to ``'mapBoundingBox'``.

        Accepts either:

          * ``'mapBoundingBox'`` (default)
          * ``'plotBox'``

        .. note::

          If ``'plotBox'``, they will be fixed to the plot box and responsively move in
          relation to the main map.

          If ``'mapBoundingBox'``, they will be fixed to the map bounding box, which is
          constant and centered in different chart sizes and ratios.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._relative_to

    @relative_to.setter
    def relative_to(self, value):
        if not value:
            self._relative_to = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['mapBoundingBox', 'plotBox']:
                raise errors.HighchartsValueError(f'relative_to expects either '
                                                  f'"mapBoundingBox" or "plotBox". '
                                                  f'Received: "{value}"')
            self._relative_to = value

    @property
    def units(self) -> Optional[str]:
        """The units to use for the inset's
        :meth:`.field <highcharts_maps.options.map_views.insets.Inset.field>` and
        :meth:`.border_path <highcharts_maps.options.map_views.insets.Inset.border_path>`
        settings. Defaults to ``'percent'``.

        Accepts either:

          * ``'percent'`` (default)
          * ``'pixels'``

        .. note::

          If ``'percent'``, they are expressed as a percentage of the item referenced in
          :meth:`.relative_to <highcharts_maps.options.map_views.insets.Inset.relative_to>`.

          If ``'pixels'``, they are expressed in absolute values.

        :rtype: :class:`str <python:str>`
        """
        return self._units

    @units.setter
    def units(self, value):
        if not value:
            self._units = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['percent', 'pixels']:
                raise errors.HighchartsValueError(f'units expects either "percent" or '
                                                  f'"pixels". Received: "{value}".')
            self._units = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'padding': as_dict.get('padding', None),
            'relative_to': as_dict.get('relativeTo', None),
            'units': as_dict.get('units', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'padding': self.padding,
            'relativeTo': self.relative_to,
            'units': self.units,
        }

        return untrimmed


class Inset(InsetOptions):
    """Configuration of a specific :term:`map inset`."""

    def __init__(self, **kwargs):
        self._border_path = None
        self._field = None
        self._geo_bounds = None
        self._id = None
        self._projection = None

        self.border_path = kwargs.get('border_path', None)
        self.field = kwargs.get('field', None)
        self.geo_bounds = kwargs.get('geo_bounds', None)
        self.projection = kwargs.get('projection', None)

        super().__init__(**kwargs)

    @property
    def border_path(self) -> Optional[MultiLineString]:
        """A :class:`MultiLineString <highcharts_maps.utility_classes.geojson.MultiLineString>`
        geometry that defines the border path of the inset in units as per
        :meth:`.units <highcharts_maps.options.map_views.insets.Inset.units>`. Defaults to
        :obj:`None <python:None>`.

        If :obj:`None <python:None>`, a border is rendered around the
        :meth:`.field <highcharts_maps.options.map_views.insets.Inset.field>` geometry.

        .. tip::

          **Best practice!**

          It is recommended that the border path partly follows the outline of the field
          in order to make pointer positioning consistent.

        :rtype: :class:`MultiLineString <highcharts_maps.utility_classes.geojson.MultiLineString>`
          or :obj:`None <python:None>`
        """
        return self._border_path

    @border_path.setter
    @class_sensitive(MultiLineString)
    def border_path(self, value):
        self._border_path = value

    @property
    def field(self) -> Optional[Polygon]:
        """A :class:`Polygon <highcharts_maps.utility_classes.geojson.Polygon>` geometry
        that defines where in the chart the inset should be rendered in units as per
        :meth:`.units <highcharts_maps.options.map_views.insets.Inset.units>`. Defaults to
        :obj:`None <python:None>`.

        If :obj:`None <python:None>`, the inset is rendered in the full plot area.

        :rtype: :class:`Polygon <highcharts_maps.utility_classes.geojson.Polygon>` or
          :obj:`None <python:None>`
        """
        return self._field

    @field.setter
    @class_sensitive(Polygon)
    def field(self, value):
        self._field = value

    @property
    def geo_bounds(self) -> Optional[Polygon]:
        """A :class:`Polygon <highcharts_maps.utility_classes.geojson.Polygon>` geometry
        that encircles the shapes that should be rendered inside the inset. Geometries
        that are found within this geometry are removed from the default map view and
        rendered in the inset. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`Polygon <highcharts_maps.utility_classes.geojson.Polygon>` or
          :obj:`None <python:None>`
        """
        return self._geo_bounds

    @geo_bounds.setter
    @class_sensitive(Polygon)
    def geo_bounds(self, value):
        self._geo_bounds = value

    @property
    def id(self) -> Optional[str]:
        """The identifier given to the inset. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def projection(self) -> Optional[ProjectionOptions]:
        """The projection options for the inset. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`ProjectionOptions <highcharts_maps.utility_classes.projection.ProjectionOptions>`
          or :obj:`None <python:None>`
        """
        return self._projection

    @projection.setter
    @class_sensitive(ProjectionOptions)
    def projection(self, value):
        self._projection = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'padding': as_dict.get('padding', None),
            'relative_to': as_dict.get('relativeTo', None),
            'units': as_dict.get('units', None),

            'border_path': as_dict.get('borderPath', None),
            'field': as_dict.get('field', None),
            'geo_bounds': as_dict.get('geoBounds', None),
            'id': as_dict.get('id', None),
            'projection': as_dict.get('projection', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderPath': self.border_path,
            'field': self.field,
            'geoBounds': self.geo_bounds,
            'id': self.id,
            'projection': self.projection
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
