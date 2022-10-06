from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_maps.decorators import class_sensitive
from highcharts_maps.metaclasses import HighchartsMeta
from highcharts_maps.utility_classes.buttons import MapButtonConfiguration


class MapButtonOptions(HighchartsMeta):
    """Configuration of individual buttons for map navigation.

    .. note::

      The
      :meth:`.onclick <highcharts_maps.utility_classes.buttons.MapButtonConfiguration.onclick>`,
      :meth:`.text <highcharts_maps.utility_classes.buttons.MapButtonConfiguration.text>`,
      and :meth:`.y <highcharts_maps.utility_classes.buttons.MapButtonConfiguration.y>`
      properties are configured individually, but other properties will inherit from
      :meth:`.button_options <highcharts_maps.options.map_navigation.MapNavigationOptions.button_options>`
      unless overridden.

    """

    def __init__(self, **kwargs):
        self._zoom_in = None
        self._zoom_out = None

        self.zoom_in = kwargs.get('zoom_in', None)
        self.zoom_out = kwargs.get('zoom_out', None)

    @property
    def zoom_in(self) -> Optional[MapButtonConfiguration]:
        """Options for the zoom in button. Defaults to :obj:`None <python:None>`

        :rtype: :class:`MapButtonConfiguration <highcharts_maps.utility_classes.buttons.MapButtonConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._zoom_in

    @zoom_in.setter
    @class_sensitive(MapButtonConfiguration)
    def zoom_in(self, value):
        self._zoom_in = value

    @property
    def zoom_out(self) -> Optional[MapButtonConfiguration]:
        """Options for the zoom out button. Defaults to :obj:`None <python:None>`

        :rtype: :class:`MapButtonConfiguration <highcharts_maps.utility_classes.buttons.MapButtonConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._zoom_out

    @zoom_out.setter
    @class_sensitive(MapButtonConfiguration)
    def zoom_out(self, value):
        self._zoom_out = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'zoom_in': as_dict.get('zoomIn', None),
            'zoom_out': as_dict.get('zoomOut', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'zoomIn': self.zoom_in,
            'zoomOut': self.zoom_out
        }

        return untrimmed


class MapNavigationOptions(HighchartsMeta):
    """Configuration options for the buttons that handle navigation and zooming within
    map visualizations."""

    def __init__(self, **kwargs):
        self._button_options = None
        self._buttons = None
        self._enable_buttons = None
        self._enabled = None
        self._enable_double_click_zoom = None
        self._enable_double_click_zoom_to = None
        self._enable_mouse_wheel_zoom = None
        self._enable_touch_zoom = None
        self._mouse_wheel_sensitivity = None

        self.button_options = kwargs.get('button_options', None)
        self.buttons = kwargs.get('buttons', None)
        self.enable_buttons = kwargs.get('enable_buttons', None)
        self.enabled = kwargs.get('enabled', None)
        self.enable_double_click_zoom = kwargs.get('enable_double_click_zoom', None)
        self.enable_double_click_zoom_to = kwargs.get('enable_double_click_zoom_to', None)
        self.enable_mouse_wheel_zoom = kwargs.get('enable_mouse_wheel_zoom', None)
        self.enable_touch_zoom = kwargs.get('enable_touch_zoom', None)
        self.mouse_wheel_sensitivity = kwargs.get('mouse_wheel_sensitivity', None)

    @property
    def button_options(self) -> Optional[MapButtonConfiguration]:
        """General configuration options for the map navigation buttons. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Specific configurations for individual map navigation buttons can be set using
          :meth:`MapNavigationOptions.buttons <highcharts_maps.options.map_navigation.MapNavigationOptions.buttons>`.

        :rtype: :class:`MapButtonConfiguration <highcharts_maps.utility_classes.buttons.MapButtonConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._button_options

    @button_options.setter
    @class_sensitive(MapButtonConfiguration)
    def button_options(self, value):
        self._button_options = value

    @property
    def buttons(self) -> Optional[MapButtonOptions]:
        """Configuration of individual buttons for map navigation.

        .. note::

          The
          :meth:`.onclick <highcharts_maps.utility_classes.buttons.MapButtonConfiguration.onclick>`,
          :meth:`.text <highcharts_maps.utility_classes.buttons.MapButtonConfiguration.text>`,
          and :meth:`.y <highcharts_maps.utility_classes.buttons.MapButtonConfiguration.y>`
          properties are configured individually, but other properties will inherit from
          :meth:`.button_options <highcharts_maps.options.map_navigation.MapNavigationOptions.button_options>`
          unless overridden.

        :rtype: :class:`MapButtonOptions` or :obj:`None <python:None>`
        """
        return self._buttons

    @buttons.setter
    @class_sensitive(MapButtonOptions)
    def buttons(self, value):
        self._buttons = value

    @property
    def enable_buttons(self) -> Optional[bool]:
        """Whether to enable map navigation buttons. If :obj:`None <python:None>`, applies
        the value from
        :meth:`.enabled <highcharts_maps.options.map_navigation.MapNavigationOptions.enabled>`.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enable_buttons

    @enable_buttons.setter
    def enable_buttons(self, value):
        if value is None:
            self._enable_buttons = None
        else:
            self._enable_buttons = bool(value)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables map navigation. Defaults to ``False``.

        .. warning::

          The default is to *disable* map navigation because:

            * Many :term:`choropleth maps <choropleth map>` are simple and do not need it
            * When touch zoom and mouse wheel zoom are enabled, default interactions will
              break and must be individually applied.

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
    def enable_double_click_zoom(self) -> Optional[bool]:
        """If ``True``, enables zooming by double clicking on the map. If
        :obj:`None <python:None>`, applies the value from
        :meth:`.enabled <highcharts_maps.options.map_navigation.MapNavigationOptions.enabled>`.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enable_double_click_zoom

    @enable_double_click_zoom.setter
    def enable_double_click_zoom(self, value):
        if value is None:
            self._enable_double_click_zoom = None
        else:
            self._enable_double_click_zoom = bool(value)

    @property
    def enable_double_click_zoom_to(self) -> Optional[bool]:
        """If ``True``, enables zooming into a specific area by double clicking on that
        area. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enable_double_click_zoom_to

    @enable_double_click_zoom_to.setter
    def enable_double_click_zoom_to(self, value):
        if value is None:
            self._enable_double_click_zoom_to = None
        else:
            self._enable_double_click_zoom_to = bool(value)

    @property
    def enable_mouse_wheel_zoom(self) -> Optional[bool]:
        """If ``True``, enables zooming using the mouse wheel. If
        :obj:`None <python:None>`, applies the value from
        :meth:`.enabled <highcharts_maps.options.map_navigation.MapNavigationOptions.enabled>`.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enable_mouse_wheel_zoom

    @enable_mouse_wheel_zoom.setter
    def enable_mouse_wheel_zoom(self, value):
        if value is None:
            self._enable_mouse_wheel_zoom = None
        else:
            self._enable_mouse_wheel_zoom = bool(value)

    @property
    def enable_touch_zoom(self) -> Optional[bool]:
        """If ``True``, enables multi-touch zooming. If
        :obj:`None <python:None>`, applies the value from
        :meth:`.enabled <highcharts_maps.options.map_navigation.MapNavigationOptions.enabled>`.
        Defaults to :obj:`None <python:None>`.

        .. warning::

          If the chart covers the viewport, setting this to ``True`` will prevent the user
          from being able to use multi-touch zoom on the website that contains the chart.
          This behavior can be counter-intuitive, so you should take steps to ensure the
          user (particularly using mobile devices) does not get "stuck" within the chart.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enable_touch_zoom

    @enable_touch_zoom.setter
    def enable_touch_zoom(self, value):
        if value is None:
            self._enable_touch_zoom = None
        else:
            self._enable_touch_zoom = bool(value)

    @property
    def mouse_wheel_sensitivity(self) -> Optional[int | float | Decimal]:
        """Sensitivity of mouse wheel or trackpad scrolling. ``1`` is no sensitivity, while
        a setting of ``2`` means that one rotation of the mouse wheel will zoom in 50%.
        Defaults to ``1.1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._mouse_wheel_sensitivity

    @mouse_wheel_sensitivity.setter
    def mouse_wheel_sensitivity(self, value):
        self._mouse_wheel_sensitivity = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'button_options': as_dict.get('buttonOptions', None),
            'buttons': as_dict.get('buttons', None),
            'enable_buttons': as_dict.get('enableButtons', None),
            'enabled': as_dict.get('enabled', None),
            'enable_double_click_zoom': as_dict.get('enableDoubleClickZoom', None),
            'enable_double_click_zoom_to': as_dict.get('enableDoubleClickZoomTo', None),
            'enable_mouse_wheel_zoom': as_dict.get('enableMouseWheelZoom', None),
            'enable_touch_zoom': as_dict.get('enableTouchZoom', None),
            'mouse_wheel_sensitivity': as_dict.get('mouseWheelSensitivity', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'buttonOptions': self.button_options,
            'buttons': self.buttons,
            'enableButtons': self.enable_buttons,
            'enabled': self.enabled,
            'enableDoubleClickZoom': self.enable_double_click_zoom,
            'enableDoubleClickZoomTo': self.enable_double_click_zoom_to,
            'enableMouseWheelZoom': self.enable_mouse_wheel_zoom,
            'enableTouchZoom': self.enable_touch_zoom,
            'mouseWheelSensitivity': self.mouse_wheel_sensitivity,
        }

        return untrimmed
