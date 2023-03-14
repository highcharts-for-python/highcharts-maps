from typing import Optional

from validator_collection import validators

from highcharts_core.global_options.language import Language as LanguageBase


class Language(LanguageBase):
    """Collection of configuration settings for UI strings that can be adapted for
    display in specific languages.

    .. note::

      The :class:`Language` object is a global setting in Highcharts and it *cannot* be
      set on each chart initialization. Instead, it has to be set using (in JavaScript)
      ``Highcharts.setOptions(...)`` before any chart is initialized.

    """

    def __init__(self, **kwargs):
        self._zoom_in = None
        self._zoom_out = None

        self.zoom_in = kwargs.get('zoom_in', None)
        self.zoom_out = kwargs.get('zoom_out', None)

        super().__init__(**kwargs)

    @property
    def zoom_in(self) -> Optional[str]:
        """The title that appears when hovering over the zoom in button. Defaults to
        ``'+'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zoom_in

    @zoom_in.setter
    def zoom_in(self, value):
        self._zoom_in = validators.string(value, allow_empty = True)

    @property
    def zoom_out(self) -> Optional[str]:
        """The title that appears when hovering over the zoom out button. Defaults to
        ``'-'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zoom_out

    @zoom_out.setter
    def zoom_out(self, value):
        self._zoom_out = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'context_button_title': as_dict.get('contextButtonTitle', None),
            'decimal_point': as_dict.get('decimalPoint', None),
            'download_csv': as_dict.get('downloadCSV', None),
            'download_jpeg': as_dict.get('downloadJPEG', None),
            'download_pdf': as_dict.get('downloadPDF', None),
            'download_png': as_dict.get('downloadPNG', None),
            'download_svg': as_dict.get('downloadSVG', None),
            'download_xls': as_dict.get('downloadXLS', None),
            'drillup_text': as_dict.get('drillUpText', None),
            'exit_fullscreen': as_dict.get('exitFullscreen', None),
            'export_data': as_dict.get('exportData', None),
            'hide_data': as_dict.get('hideData', None),
            'invalid_date': as_dict.get('invalidDate', None),
            'loading': as_dict.get('loading', None),
            'main_breadcrumb': as_dict.get('mainBreadcrumb', None),
            'months': as_dict.get('months', None),
            'navigation': as_dict.get('navigation', None),
            'no_data': as_dict.get('noData', None),
            'numeric_symbol_magnitude': as_dict.get('numericSymbolMagnitude', None),
            'numeric_symbols': as_dict.get('numericSymbols', None),
            'print_chart': as_dict.get('printChart', None),
            'reset_zoom': as_dict.get('resetZoom', None),
            'reset_zoom_title': as_dict.get('resetZoomTitle', None),
            'short_months': as_dict.get('shortMonths', None),
            'short_weekdays': as_dict.get('shortWeekdays', None),
            'thousands_separator': as_dict.get('thousandsSep', None),
            'view_data': as_dict.get('viewData', None),
            'view_fullscreen': as_dict.get('viewFullscreen', None),
            'weekdays': as_dict.get('weekdays',  None),

            'zoom_in': as_dict.get('zoomIn', None),
            'zoom_out': as_dict.get('zoomOut', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'zoomIn': self.zoom_in,
            'zoomOut': self.zoom_out
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
