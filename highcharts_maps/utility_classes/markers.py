from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.utility_classes.markers import *

from highcharts_maps import errors
from highcharts_maps.metaclasses import HighchartsMeta


class FlowmapMarker(HighchartsMeta):
    """Configuration of the arrow to depict at the end of a 
    :class:`FlowmapSeries <highcharts_maps.options.series.flowmap.FlowmapSeries>`.
    """
    
    def __init__(self, **kwargs):
        self._enabled = None
        self._height = None
        self._marker_type = None
        self._width = None
        
        self.enabled = kwargs.get('enabled', None)
        self.height = kwargs.get('height', None)
        self.marker_type = kwargs.get('marker_type', None)
        self.width = kwargs.get('width', None)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays the marker on the associated series. Defaults to ``True``.

        :returns: Flag indicating whether the marker is enabled for the series.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def height(self) -> Optional[str | int | float | Decimal]:
        """The height of the marker, expressed either in pixels or as a percentage of the weight of the link. 
        Defaults to ``'40%'``.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        if value is None:
            self._height = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except (TypeError, ValueError):
                value = validators.numeric(value, minimum = 0)

            self._height = value
            
    @property
    def marker_type(self) -> Optional[str]:
        """The shape to use for the marker symbol. Accepts either ``'arrow'`` or ``'mushroom'``. Defaults to 
        ``'arrow'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._marker_type
    
    @marker_type.setter
    def marker_type(self, value):
        if not value:
            self._marker_type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['arrow', 'mushroom']:
                raise errors.HighchartsValueError(f'marker_type expects either "arrow" or "mushroom", '
                                                  f' but received "{value}".')
            self._marker_type = value
                
    @property
    def width(self) -> Optional[str | int | float | Decimal]:
        """The width of the marker, expressed either in pixels or as a percentage of the weight of the link. 
        Defaults to ``'40%'``.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        if value is None:
            self._width = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except (TypeError, ValueError):
                value = validators.numeric(value, minimum = 0)

            self._width = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'height': as_dict.get('height', None),
            'marker_type': as_dict.get('markerType', None),
            'width': as_dict.get('width', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'height': self.height,
            'markerType': self.marker_type,
            'width': self.width,
        }
        
        return untrimmed