from typing import Optional

from validator_collection import validators

from highcharts_maps.decorators import class_sensitive
from highcharts_maps.options.series.base import MapSeriesBase
from highcharts_maps.options.plot_options.tiledwebmap import TiledWebMapOptions
from highcharts_core.options.plot_options.sonification import SeriesSonification


class TiledWebMapSeries(MapSeriesBase, TiledWebMapOptions):
    """A tiled web map series allows you to display dynamically joined individual images (tiles) 
    and join them together to create a map.

    .. figure:: ../../../_static/tiledwebmap-example.png
      :alt: Tiled Web Map Example chart
      :align: center

    """
    
    def __init__(self, **kwargs):
        self._id = None
        self._index = None
        self._legend_index = None
        self._name = None
        self._sonification = None
        
        self.id = kwargs.get('id', None)
        self.index = kwargs.get('index', None)
        self.legend_index = kwargs.get('legend_index', None)
        self.name = kwargs.get('name', None)
        self.sonification = kwargs.get('sonification', None)
        
        super().__init__(**kwargs)

    @property
    def data(self):
        """
        
        .. warning::

          The ``.data`` property is *not* supported on 
          :class:`TiledWebMapSeries <highcharts_maps.options.series.tiledwebmap.TiledWebMapSeries>`, and
          so *always* returns :obj:`None <python:None>`.
          
        :rtype: :obj:`None <python:None>`.
        """
        return None
    
    @data.setter
    def data(self, value):
        self._data = None

    @property
    def id(self) -> Optional[str]:
        """An id for the series. Defaults to :obj:`None <python:None>`.

        .. hint::

          This can be used (in JavaScript) after render time to get a pointer to the
          series object through ``chart.get()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def index(self) -> Optional[int]:
        """The index for the series in the chart, affecting the internal index in the
        (JavaScript) ``chart.series`` array, the visible Z-index, and the order of the
        series in the legend. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._index

    @index.setter
    def index(self, value):
        self._index = validators.integer(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def legend_index(self) -> Optional[int]:
        """The sequential index for the series in the legend. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._legend_index

    @legend_index.setter
    def legend_index(self, value):
        self._legend_index = validators.integer(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def name(self) -> Optional[str]:
        """The name of the series as shown in the legend, tooltip, etc. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def sonification(self) -> Optional[SeriesSonification]:
        """Sonification configuration for the series type/series.
        
        :rtype: :class:`SeriesSonification <highcharts_core.options.plot_options.sonification.SeriesSonification>` or
          :obj:`None <python:None>`
        """
        return self._sonification
    
    @sonification.setter
    @class_sensitive(SeriesSonification)
    def sonification(self, value):
        self._sonification = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'map_data': as_dict.get('mapData', None),
            
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'opacity': as_dict.get('opacity', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'provider': as_dict.get('provider', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'states': as_dict.get('states', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),
            
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'sonification': as_dict.get('sonification', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'id': self.id,
            'index': self.index,
            'legendIndex': self.legend_index,
            'name': self.name,
            'sonification': self.sonification,
            
            'mapData': self.map_data,
            
            'accessibility': self.accessibility,
            'className': self.class_name,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'includeInDataExport': self.include_in_data_export,
            'legendSymbol': self.legend_symbol,
            'opacity': self.opacity,
            'pointDescriptionFormat': self.point_description_format,
            'provider': self.provider,
            'showInLegend': self.show_in_legend,
            'skipKeyboardNavigation': self.skip_keyboard_navigation,
            'states': self.states,
            'visible': self.visible,
            'type': self.type,
            'zIndex': self.z_index,
        }

        return untrimmed

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return GeometricDataCollection

    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return GeometricData
