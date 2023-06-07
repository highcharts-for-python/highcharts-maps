from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_maps import errors
from highcharts_maps.decorators import class_sensitive
from highcharts_maps.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts_core.options.plot_options.accessibility import TypeOptionsAccessibility
from highcharts_core.utility_classes.events import SeriesEvents
from highcharts_core.utility_classes.states import States


class ProviderOptions(HighchartsMeta):
    """Configuration of options enabling conncetion to the provider from which map images 
    (tiles) will be retrieved."""
    
    def __init__(self, **kwargs):
        self._api_key = None
        self._subdomain = None
        self._theme = None
        self._type = None
        self._url = None
        
        self.api_key = kwargs.get('api_key', None)
        self.subdomain = kwargs.get('subdomain', None)
        self.theme = kwargs.get('theme', None)
        self.type = kwargs.get('type', None)
        self.url = kwargs.get('url', None)
        
    @property
    def api_key(self) -> Optional[str]:
        """API key used to authenticate against the provider. Applicable if the provider uses an API key.
        Defaults to :obj:`None <python:None>`.
        
        :rtype: :class:`str <python:str>`
        """
        return self._api_key
    
    @api_key.setter
    def api_key(self, value):
        self._api_key = validators.string(value, allow_empty = True)
        
    @property
    def subdomain(self) -> Optional[str]:
        """Subdomain required by the provider. Defaults to :obj:`None <python:None>`.
        
        .. note::
        
          Different providers require different subdomains to be specified. For more
          information, please see 
          `Tiled Web Map Configuration: Providers Properties <https://www.highcharts.com/docs/maps/tiledwebmap#providers-properties>`__
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._subdomain
    
    @subdomain.setter
    def subdomain(self, value):
        self._subdomain = validators.string(value, allow_empty = True)
        
    @property
    def theme(self) -> Optional[str]:
        """The tile theme to apply. Defaults to :obj:`None <python:None>`.
        
        .. note::
        
          Different providers offer different themes for their map tiles. For more
          information, please see 
          `Tiled Web Map Configuration: Providers Properties <https://www.highcharts.com/docs/maps/tiledwebmap#providers-properties>`__

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._theme
    
    @theme.setter
    def theme(self, value):
        self._theme = validators.string(value, allow_empty = True)
        
    @property
    def type(self) -> Optional[str]:
        """Indication of the provider to use, if not using a custom provider.
        Defaults to :obj:`None <python:None>`.
        
        .. warning:: 
        
          The value is **case-sensitive**.
        
        The following are provider types that are (currently) known / recognized:
        
          * ``'OpenStreetMap'``
          * ``'Thunderforest'``
          * ``'Esri'``
          * ``'Stamen'``
          * ``'USGS'``
          * ``'LimaLabs'``
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = validators.string(value, allow_empty = True)
        
    @property
    def url(self) -> Optional[str]:
        """Custom URL to use for a provider that is not identified using 
        :meth:`.type <highcharts_maps.options.plot_options.tiledwebmap.ProviderOptions.type>`.
        
        The following variables are available to use, for example in URL parameters:
        
          * ``'{x}'``
          * ``'{y}'``
          * ``'{z}'``
          * ``'{zoom}'``
          
        .. warning::
        
          Remember to always specify a projection when using a custom URL!
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._url

    @url.setter
    def url(self, value):
        self._url = validators.url(value, allow_empty = True)

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
            'api_key': as_dict.get('apiKey', None),
            'subdomain': as_dict.get('subdomain', None),
            'theme': as_dict.get('theme', None),
            'type': as_dict.get('type', None),
            'url': as_dict.get('url', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'apiKey': self.api_key,
            'subdomain': self.subdomain,
            'theme': self.theme,
            'type': self.type,
            'url': self.url,
        }

        return untrimmed


class TiledWebMapOptions(HighchartsMeta):
    """A tiled web map series allows you to display dynamically joined individual images (tiles) 
    and join them together to create a map.

    .. figure:: ../../../_static/tiledwebmap-example.png
      :alt: Tiled Web Map Example chart
      :align: center

    """
    
    def __init__(self, **kwargs):
        self._accessibility = None
        self._class_name = None
        self._custom = None
        self._description = None
        self._events = None
        self._include_in_data_export = None
        self._legend_symbol = None
        self._opacity = None
        self._point_description_format = None
        self._provider = None
        self._show_in_legend = None
        self._skip_keyboard_navigation = None
        self._states = None
        self._visible = None
        self._z_index = None
        
        self.accessibility = kwargs.get('accessibility', None)
        self.class_name = kwargs.get('class_name', None)
        self.custom = kwargs.get('custom', None)
        self.description = kwargs.get('description', None)
        self.events = kwargs.get('events', None)
        self.include_in_data_export = kwargs.get('include_in_data_export', None)
        self.legend_symbol = kwargs.get('legend_symbol', None)
        self.opacity = kwargs.get('opacity', None)
        self.point_description_format = kwargs.get('point_description_format', None)
        self.provider = kwargs.get('provider', None)
        self.show_in_legend = kwargs.get('show_in_legend', None)
        self.skip_keyboard_navigation = kwargs.get('skip_keyboard_navigation', None)
        self.states = kwargs.get('states', None)
        self.visible = kwargs.get('visible', None)
        self.z_index = kwargs.get('z_index', None)
        
    @property
    def type(self) -> str:
        """Indicates the type of series that is represented by this instance.

        .. warning::

          This proprety is read-only!

        :rtype: :class:`str <python:str>`
        """
        class_name = self.__class__.__name__
        class_name = class_name.replace('TypeOptions', '')
        class_name = class_name.replace('Options', '')
        if class_name.endswith('Series') and class_name != 'Series':
            class_name = class_name.replace('Series', '')

        return class_name.lower()

    @type.setter
    def type(self, value):
        raise errors.HighchartsReadOnlyError('type is a read-only property and cannot be '
                                             'set manually')

    @property
    def accessibility(self) -> Optional[TypeOptionsAccessibility]:
        """Accessibility options for a series.

        :rtype: :class:`TypeOptionsAccessibility` or :obj:`None <python:None>`
        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(TypeOptionsAccessibility)
    def accessibility(self, value):
        self._accessibility = value

    @property
    def class_name(self) -> Optional[str]:
        """The additional CSS class name to apply to the series' graphical elements.

        .. note::

          This option is additive to the default class names - it does not replace them.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def custom(self) -> Optional[JavaScriptDict]:
        """A reserved subspace to store options and values for customized functionality.

        Here you can add additional data for your own event callbacks and formatter
        callbacks.

        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._custom

    @custom.setter
    @class_sensitive(JavaScriptDict)
    def custom(self, value):
        self._custom = value

    @property
    def description(self) -> Optional[str]:
        """A description of the series to add to the screen reader information about the
        series.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @property
    def events(self) -> Optional[SeriesEvents]:
        """General event handlers for the series items.

        .. note::

          These event hooks can also be attached to the series at run time using the
          (JavaScript) ``Highcharts.addEvent()`` function.

        :rtype: :class:`SeriesEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(SeriesEvents)
    def events(self, value):
        self._events = value

    @property
    def include_in_data_export(self) -> Optional[bool]:
        """If ``False``, will prevent the data series from being included in any form of
        data export. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._include_in_data_export

    @include_in_data_export.setter
    def include_in_data_export(self, value):
        if value is None:
            self._include_in_data_export = None
        else:
            self._include_in_data_export = bool(value)

    @property
    def legend_symbol(self) -> Optional[str]:
        """The type of legend symbol to render for the series. Accepts either 
        ``'lineMarker'`` or ``'rectangle'``. Defaults to ``'rectangle'``.
        
        :rtype: :class:`str <python:str>`
        """
        return self._legend_symbol
    
    @legend_symbol.setter
    def legend_symbol(self, value):
        if not value:
            self._legend_symbol = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value == 'linemarker':
                value = 'lineMarker'
            if value not in ['lineMarker', 'rectangle']:
                raise errors.HighchartsValueError(f'legend_symbol expects either '
                                                  f'"lineMarker" or "rectangle". '
                                                  f'Received: "{value}".')
            self._legend_symbol = value

    @property
    def opacity(self) -> Optional[float]:
        """Opacity of a series parts: line, fill (e.g. area), and labels.

        :rtype: :class:`float <python:float>`
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = validators.float(value,
                                         allow_empty = True,
                                         minimum = 0.0,
                                         maximum = 1.0)

    @property
    def point_description_format(self) -> Optional[str]:
        """A :term:`format string` to use instead of the default for 
        point descriptions on the series. Defaults to :obj:`None <python:None>`.
        
        .. note::
        
          Overrides the chart-wide configuration, as applicable.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_description_format
    
    @point_description_format.setter
    def point_description_format(self, value):
        self._point_description_format = validators.string(value, allow_empty = True)

    @property
    def provider(self) -> Optional[ProviderOptions]:
        """"""
        return self._provider
    
    @provider.setter
    @class_sensitive(ProviderOptions)
    def provider(self, value):
        self._provider = value
        
    @property
    def show_in_legend(self) -> Optional[bool]:
        """Whether to display this particular series or series type in the legend.
        Standalone series are shown in the legend by default, and linked series are not.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_in_legend

    @show_in_legend.setter
    def show_in_legend(self, value):
        if value is None:
            self._show_in_legend = None
        else:
            self._show_in_legend = bool(value)

    @property
    def skip_keyboard_navigation(self) -> Optional[bool]:
        """If ``True``, the accessibility module will skip past this series when executing
        keyboard navigation.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._skip_keyboard_navigation

    @skip_keyboard_navigation.setter
    def skip_keyboard_navigation(self, value):
        if value is None:
            self._skip_keyboard_navigation = None
        else:
            self._skip_keyboard_navigation = bool(value)

    @property
    def states(self) -> Optional[States]:
        """Configuration for state-specific configuration to apply to the data series.

        :rtype: :class:`States` or :obj:`None <python:None>`
        """
        return self._states

    @states.setter
    @class_sensitive(States)
    def states(self, value):
        self._states = value

    @property
    def visible(self) -> Optional[bool]:
        """If ``True``, the series is initially visible. If ``False``, the series is
        hidden by default. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value is None:
            self._visible = None
        else:
            self._visible = bool(value)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """Z-index of the series. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)

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
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
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
