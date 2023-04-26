from typing import Optional
from highcharts_core.options.drilldown import Drilldown as DrilldownBase

from highcharts_maps.utility_functions import mro__to_untrimmed_dict


class Drilldown(DrilldownBase):
    """Options to configure :term:`drilldown` functionality in the chart, which
    enables users to inspect increasingly high resolution data by clicking on chart
    items like columns or pie slices.

    .. note::

      The drilldown feature requires the ``drilldown.js`` file to be loaded in the
      browser/client. This file is found in the modules directory of the download
      package, or online at
      `code.highcharts.com/modules/drilldown.js <code.highcharts.com/modules/drilldown.js>`_.

    """

    def __init__(self, **kwargs):
        self._map_zooming = None

        self.map_zooming = kwargs.get('map_zooming', None)

        super().__init__(**kwargs)

    @property
    def map_zooming(self) -> Optional[bool]:
        """Enable or disable zooming into a region of a clicked map point that you wish to drill into. Defaults
        to ``True``. If ``False``, the drilldown/drillup animations only fade in/out without zooming to a specific 
        map point.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._map_zooming
    
    @map_zooming.setter
    def map_zooming(self, value):
        if value is None:
            self._map_zooming = None
        else:
            self._map_zooming = bool(value)
            
    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'active_axis_label_style': as_dict.get('activeAxisLabelStyle', None),
            'active_data_label_style': as_dict.get('activeDataLabelStyle', None),
            'allow_point_drilldown': as_dict.get('allowPointDrilldown', None),
            'animation': as_dict.get('animation', None),
            'breadcrumbs': as_dict.get('breadcrumbs', None),
            'series': as_dict.get('series', None),
            
            'map_zooming': as_dict.get('mapZooming', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'map_zooming': self.map_zooming
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
