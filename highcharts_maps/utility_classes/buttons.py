from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.utility_classes.buttons import (ButtonTheme,
                                                     ButtonConfiguration,
                                                     ContextButtonConfiguration,
                                                     ExportingButtons)

from highcharts_maps import errors


class MapButtonConfiguration(ButtonConfiguration):
    """General configuration options for the map navigation buttons."""

    def __init__(self, **kwargs):
        self._align = None
        self._align_to = None
        self._height = None
        self._padding = None
        self._style = None
        self._vertical_align = None
        self._width = None
        self._x = None

        self.align = kwargs.get('align', None)
        self.align_to = kwargs.get('align_to', None)
        self.height = kwargs.get('height', None)
        self.padding = kwargs.get('padding', None)
        self.style = kwargs.get('style', None)
        self.vertical_align = kwargs.get('vertical_align', None)
        self.width = kwargs.get('width', None)
        self.x = kwargs.get('x', None)

        super().__init__(**kwargs)

    @property
    def align(self) -> Optional[str]:
        """The horizontal alignment of the navigation buttons. Defaults to ``'left'``.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._align

    @align.setter
    def align(self, value):
        if not value:
            self._align = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'align accepts "left", "center", or '
                                                  f'"right". Was: "{value}"')

            self._align = value

    @property
    def align_to(self) -> Optional[str]:
        """Setting of what box the buttons should align to. Accepts:

          * ``'plotBox'``
          * ``'spacingBox'``

        Defaults to ``'plotBox'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._align_to

    @align_to.setter
    def align_to(self, value):
        if not value:
            self._align_to = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['plotBox', 'spacingBox']:
                raise errors.HighchartsValueError(f'align_to accepts "plotBox", '
                                                  f'"spacingBox". Was: "{value}"')

            self._align_to = value

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """The height of the map navigation buttons, expressed in pixels. Defaults to
        ``18``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def padding(self) -> Optional[int | float | Decimal]:
        """Padding to apply to the navigation buttons, expressed in pixels. Defaults to
        ``5``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = validators.numeric(value, allow_empty = True)

    @property
    def style(self) -> Optional[str]:
        """Text styles for the map navigation buttons. Defaults to
        ``'{"fontSize": "15px", "fontWeight": "bold"}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @property
    def vertical_align(self) -> Optional[str]:
        """The vertical alignment of the navigation buttons. Defaults to ``'top'``.

        Accepts:

          * ``'top'``
          * ``'middle'``
          * ``'bottom'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_align

    @vertical_align.setter
    def vertical_align(self, value):
        if not value:
            self._vertical_align = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['top', 'middle', 'bottom']:
                raise errors.HighchartsValueError(f'vertical_align accepts "top", '
                                                  f'"middle", or '
                                                  f'"bottom". Was: "{value}"')

            self._vertical_align = value

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """The width of the map navigation buttons, expressed in pixels. Defaults to
        ``18``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The horizontal offset of the map navigation buttons, relative to the
        :meth:`.align <highcharts_maps.utility_classes.buttons.MapButtonConfiguration.align>`
        setting. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'text': as_dict.get('text', None),
            'theme': as_dict.get('theme', None),
            'y': as_dict.get('y', None),

            'align': as_dict.get('align', None),
            'align_to': as_dict.get('alignTo', None),
            'height': as_dict.get('height', None),
            'padding': as_dict.get('padding', None),
            'style': as_dict.get('style', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'width': as_dict.get('width', None),
            'x': as_dict.get('x', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'alignTo': self.align_to,
            'height': self.height,
            'padding': self.padding,
            'style': self.style,
            'verticalAlign': self.vertical_align,
            'width': self.width,
            'x': self.x,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
