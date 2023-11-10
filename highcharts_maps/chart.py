from typing import Optional, List
from collections import UserDict

from validator_collection import validators, checkers

from highcharts_core.chart import Chart as ChartBase

from highcharts_maps import errors, utility_functions
from highcharts_maps.options import HighchartsOptions, HighchartsMapsOptions
from highcharts_maps.decorators import validate_types
from highcharts_maps.js_literal_functions import serialize_to_js_literal
from highcharts_maps.headless_export import ExportServer
from highcharts_maps.options.series.series_generator import (create_series_obj,
                                                             SERIES_CLASSES,
                                                             MAPS_SERIES_LIST)
from highcharts_maps.global_options.shared_options import SharedMapsOptions, SharedOptions
from highcharts_maps.options.chart import ChartOptions
from highcharts_maps.options.map_views import MapViewOptions
from highcharts_maps.options.series.data.map_data import MapData
from highcharts_maps.utility_classes.projections import ProjectionOptions, CustomProjection


class Chart(ChartBase):
    """Python representation of a Highcharts ``Chart`` object."""

    def __init__(self, **kwargs):
        self._is_maps_chart = None

        self.is_maps_chart = kwargs.get('is_maps_chart', False)

        super().__init__(**kwargs)

    def _jupyter_javascript(self, 
                            global_options = None, 
                            container = None,
                            random_slug = None,
                            retries = 3,
                            interval = 1000):
        """Return the JavaScript code which Jupyter Labs will need to render the chart.

        :param global_options: The :term:`shared options` to use when rendering the chart.
          Defaults to :obj:`None <python:None>`
        :type global_options: :class:`SharedOptions <highcharts_stock.global_options.shared_options.SharedOptions>`
          or :obj:`None <python:None>`
          
        :param container: The ID to apply to the HTML container when rendered in Jupyter Labs. Defaults to
          :obj:`None <python:None>`, which applies the :meth:`.container <highcharts_core.chart.Chart.container>` 
          property if set, and ``'highcharts_target_div'`` if not set.
        :type container: :class:`str <python:str>` or :obj:`None <python:None>`

        :param random_slug: The random sequence of characters to append to the container name to ensure uniqueness.
          Defaults to :obj:`None <python:None>`
        :type random_slug: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param retries: The number of times to retry rendering the chart. Used to avoid race conditions with the 
          Highcharts script. Defaults to 3.
        :type retries: :class:`int <python:int>`
        
        :param interval: The number of milliseconds to wait between retrying rendering the chart. Defaults to 1000 (1 
          seocnd).
        :type interval: :class:`int <python:int>`

        :rtype: :class:`str <python:str>`
        """
        original_container = self.container
        new_container = container or self.container or 'highcharts_target_div'
        if not random_slug:
            self.container = new_container
        else:
            self.container = f'{new_container}_{random_slug}'
        
        if global_options is not None:
            global_options = validate_types(global_options,
                                            types = (SharedMapsOptions, SharedOptions))

        js_str = ''
        js_str += utility_functions.get_retryHighcharts()

        if global_options:
            js_str += '\n' + utility_functions.prep_js_for_jupyter(global_options.to_js_literal()) + '\n'

        js_str += utility_functions.prep_js_for_jupyter(self.to_js_literal(),
                                                        container = self.container,
                                                        random_slug = random_slug,
                                                        retries = retries,
                                                        interval = interval)

        self.container = original_container

        return js_str

    def get_required_modules(self, include_extension = False) -> List[str]:
        """Return the list of URLs from which the Highcharts JavaScript modules
        needed to render the chart can be retrieved.
        
        :param include_extension: if ``True``, will return script names with the 
          ``'.js'`` extension included. Defaults to ``False``.
        :type include_extension: :class:`bool <python:bool>`

        :rtype: :class:`list <python:list>`
        """
        initial_scripts = ['highcharts']
        if self.is_maps_chart:
            initial_scripts.extend(['maps/modules/map',
                                    'modules/exporting'])

        scripts = self._process_required_modules(initial_scripts, include_extension)

        return scripts

    @property
    def is_maps_chart(self) -> bool:
        """If ``True``, indicates that the chart should be rendered as a
        `Highcharts Maps <https://www.highcharts.com/products/maps/>`__ chart. If
        ``False``, the chart will be rendered using the standard
        `Highcharts JS <https://www.highcharts.com/products/highcharts/>`__ constructor.
        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._is_maps_chart

    @is_maps_chart.setter
    def is_maps_chart(self, value):
        self._is_maps_chart = bool(value)

    @property
    def options(self) -> Optional[HighchartsOptions | HighchartsMapsOptions]:
        """The Python representation of the
        `Highcharts Maps <https://www.highcharts.com/products/maps/>`__
        ``options`` `configuration object <https://api.highcharts.com/highmaps/>`_
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`HighchartsOptions` or :class:`HighchartsMapsOptions` or
          :obj:`None <python:None>`
        """
        return self._options

    @options.setter
    def options(self, value):
        if not value:
            self._options = None
        elif self.is_maps_chart:
            self._options = validate_types(value, HighchartsMapsOptions)
            self.is_maps_chart = True
        else:
            if checkers.is_type(value, 'HighchartsMapsOptions'):
                self._options = value
                self.is_maps_chart = True
            elif checkers.is_type(value, 'HighchartsOptions'):
                self._options = value
            elif ('mapNavigation' in value
                  or 'map_navigation' in value
                  or 'mapView' in value
                  or 'map_view' in value):
                self._options = validate_types(value, HighchartsMapsOptions)
                self.is_maps_chart = True
            else:
                self._options = validate_types(value, HighchartsOptions)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'callback': as_dict.get('callback', None),
            'container': as_dict.get('container', None) or as_dict.get('renderTo', None),
            'options': as_dict.get('options', None) or as_dict.get('userOptions', None),
            'variable_name': as_dict.get('variable_name',
                                         None) or as_dict.get('variableName', None),

            'is_maps_chart': as_dict.get('is_maps_chart',
                                          None) or as_dict.get('isMapsChart', False)
        }

        return kwargs

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8',
                      careful_validation = False) -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :param careful_validation: if ``True``, will carefully validate JavaScript values
        along the way using the
        `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
        to ``False``.
        
        .. warning::
        
            Setting this value to ``True`` will significantly degrade serialization
            performance, though it may prove useful for debugging purposes.

        :type careful_validation: :class:`bool <python:bool>`

        .. note::

          If :meth:`variable_name <Chart.variable_name>` is set, will render a string as
          a new JavaScript instance invocation in the (pseudo-code) form:

          .. code-block:: javascript

            new VARIABLE_NAME = new Chart(...);

          If :meth:`variable_name <Chart.variable_name>` is not set, will simply return
          the ``new Chart(...)`` portion in the string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self._to_untrimmed_dict()
        as_dict = {}
        for key in untrimmed:
            item = untrimmed[key]
            serialized = serialize_to_js_literal(item,
                                                 encoding = encoding,
                                                 careful_validation = careful_validation)
            if serialized is not None:
                as_dict[key] = serialized

        signature_elements = 0

        fetch_as_str = ''
        if self.is_async:
            urls = []
            topologies = []
            if self.options.chart and self.options.chart.map:
                url = self.options.chart.map.url
                urls.append(url)
                self.options.chart.map.fetch_counter = 1

                map_data_as_str = self.options.chart.map.to_js_literal(
                    encoding = encoding,
                    careful_validation = careful_validation
                )
                topologies.append(map_data_as_str)
            
            for index, series in enumerate(self.options.series):
                if series.is_async:
                    url = series.map_data.url
                    if url in urls:
                        continue
                    urls.append(url)
                    if len(urls) > 1:
                        self.options.series[index].map_data.fetch_counter += 1
                    map_data_as_str = series.map_data.to_js_literal(
                        encoding = encoding,
                        careful_validation = careful_validation
                    )
                    topologies.append(map_data_as_str)

            fetch_as_str = '\n'.join(topologies)

        custom_projection_as_str = ''
        if self.uses_custom_projection:
            custom_projection_as_str = self.options.map_view.projection.custom.to_js_literal(
                encoding = encoding,
                careful_validation = careful_validation
            )
            custom_projection_as_str += f"""\nHighcharts.Projection.add('{self.options.map_view.projection.custom.name}', {self.options.map_view.projection.custom.class_name})\n"""

        container_as_str = ''
        if self.container:
            container_as_str = f"""'{self.container}'"""
        else:
            container_as_str = """null"""
        signature_elements += 1

        options_as_str = ''
        if self.options:
            options_as_str = self.options.to_js_literal(encoding = encoding,
                                                        careful_validation = careful_validation)
            if (
                self.is_maps_chart and 
                hasattr(self.options.chart, 'map') and 
                self.options.chart.map and 
                self.options.chart.is_async
            ):
                chart_map_str = self.options.chart.map.to_js_literal(encoding = encoding,
                                                                     careful_validation = careful_validation)
                chart_map_str = f"""'{chart_map_str}'"""
                fetch_counter = self.options.chart.map.fetch_counter
                options_as_str = options_as_str.replace(chart_map_str, f'topology{fetch_counter}')
            options_as_str = f"""{options_as_str}"""
        else:
            options_as_str = """{}"""
        signature_elements += 1

        callback_as_str = ''
        if self.callback:
            callback_as_str = self.callback.to_js_literal(encoding = encoding,
                                                          careful_validation = careful_validation)
            callback_as_str = f"""{callback_as_str}"""
            signature_elements += 1

        signature = """Highcharts.chart("""
        if self.is_maps_chart:
            signature = """Highcharts.mapChart("""
        if container_as_str:
            signature += container_as_str
            if signature_elements > 1:
                signature += ',\n'
        if options_as_str:
            signature += options_as_str
            if signature_elements > 1:
                signature += ',\n'
        if callback_as_str:
            signature += callback_as_str
        signature += ');'

        constructor_prefix = ''
        if self.variable_name:
            constructor_prefix = f'var {self.variable_name} = '

        as_str = constructor_prefix + signature

        if self.is_async:
            prefix = """document.addEventListener('DOMContentLoaded', function() {\n"""
            if custom_projection_as_str:
                prefix += custom_projection_as_str
            prefix += """(async () => { """
            suffix = """})()});"""
            as_str = fetch_as_str + '\n' + as_str
        else:
            prefix = """document.addEventListener('DOMContentLoaded', function() {\n"""
            if custom_projection_as_str:
                prefix += custom_projection_as_str
            suffix = """});"""

        as_str = prefix + as_str + '\n' + suffix

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    def download_chart(self,
                       format = 'png',
                       scale = 1,
                       width = None,
                       filename = None,
                       auth_user = None,
                       auth_password = None,
                       timeout = 0.5,
                       server_instance = None,
                       **kwargs):
        """Export a downloaded form of the chart using a Highcharts :term:`Export Server`.

        :param filename: The name of the file where the exported chart should (optionally)
          be persisted. Defaults to :obj:`None <python:None>`.
        :type filename: Path-like or :obj:`None <python:None>`

        :param auth_user: The username to use to authenticate against the
          Export Server, using :term:`basic authentication`. Defaults to
          :obj:`None <python:None>`.
        :type auth_user: :class:`str <python:str>` or :obj:`None <python:None>`

        :param auth_password: The password to use to authenticate against the Export
          Server (using :term:`basic authentication`). Defaults to
          :obj:`None <python:None>`.
        :type auth_password: :class:`str <python:str>` or :obj:`None <python:None>`

        :param timeout: The number of seconds to wait before issuing a timeout error.
          The timeout check is passed if bytes have been received on the socket in less
          than the ``timeout`` value. Defaults to ``0.5``.
        :type timeout: numeric or :obj:`None <python:None>`

        :param server_instance: Provide an already-configured :class:`ExportServer`
          instance to use to programmatically produce the exported chart. Defaults to
          :obj:`None <python:None>`, which causes Highcharts for Python to instantiate
          a new :class:`ExportServer` instance.
        :type server_instance: :class:`ExportServer` or :obj:`None <python:None>`

        .. note::

          All other keyword arguments are as per the :class:`ExportServer` constructor.

        :returns: The exported chart image, either as a :class:`bytes <python:bytes>`
          binary object or as a base-64 encoded string (depending on the ``use_base64``
          keyword argument).
        :rtype: :class:`bytes <python:bytes>` or :class:`str <python:str>`
        """
        if self.is_maps_chart:
            constructor = 'Stock'
        else:
            constructor = 'Chart'

        if not server_instance:
            return ExportServer.get_chart(filename = filename,
                                          auth_user = auth_user,
                                          auth_password = auth_password,
                                          timeout = timeout,
                                          options = self.options,
                                          constructor = constructor,
                                          scale = scale,
                                          width = width,
                                          **kwargs)

        if not isinstance(server_instance, ExportServer):
            raise errors.HighchartsValueError(f'server_instance is expected to be an '
                                              f'ExportServer instance. Was: '
                                              f'{server_instance.__class__.__name__}')

        return server_instance.request_chart(filename = filename,
                                             auth_user = auth_user,
                                             auth_password = auth_password,
                                             timeout = timeout,
                                             options = self.options,
                                             constructor = constructor,
                                             **kwargs)

    def add_series(self, *series):
        """Adds ``series`` to the
        :meth:`Chart.options.series <highcharts_core.options.HighchartsOptions.series>`
        property.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
          or coercable

        """
        new_series = []
        for item in series:
            item_series = create_series_obj(item)
            new_series.append(item_series)

        if self.options and self.options.series:
            existing_series = [x for x in self.options.series]
        elif self.options:
            existing_series = []
        else:
            existing_series = []
            if self.is_maps_chart:
                self.options = HighchartsMapsOptions()
            else:
                self.options = HighchartsOptions()

        updated_series = existing_series + new_series

        self.options.series = updated_series

    @classmethod
    def from_array(cls,
                   value,
                   series_type = 'line',
                   series_kwargs = None,
                   options_kwargs = None,
                   chart_kwargs = None,
                   is_maps_chart = False):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance with
        one series populated from the array contained in ``value``.
        
        .. seealso::

          The specific structure of the expected array is highly dependent on the type of data
          point that the series needs, which itself is dependent on the series type itself.

          Please review the detailed :ref:`series documentation <series_documentation>` for
          series type-specific details of relevant array structures.

        :param value: The array to use to populate the series data.
        :type value: iterable
        
        :param series_type: Indicates the series type that should be created from the array
          data. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`
        
        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param is_maps_chart: if ``True``, enforces the use of 
          :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`.
          If ``False``, applies 
          :class:`HighchartsOptions <highcharts_stock.options.HighchartsOptions>`.
          Defaults to ``False``.

          .. note::

            The value given to this argument will override any values specified in
            ``chart_kwargs``.

        :type is_maps_chart: :class:`bool <python:bool>`
        
        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``value``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        
        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}
        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_array(value, series_kwargs = series_kwargs)

        options_kwargs['series'] = [series]
        chart_kwargs['is_maps_chart'] = is_maps_chart

        if is_maps_chart:
            options = HighchartsMapsOptions(**options_kwargs)
        else:
            options = HighchartsOptions(**options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_series(cls, *series, kwargs = None):
        """Creates a new :class:`Chart <highcharts_core.chart.Chart>` instance populated
        with ``series``.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
          or
          :class:`IndicatorSeriesBase <highcharts_maps.options.series.base.IndicatorSeriesBase>`
          coercable

        :param kwargs: Other properties to use as keyword arguments for the instance to be
          created.

          .. warning::

            If ``kwargs`` sets the
            :meth:`options.series <highcharts_maps.options.HighchartsOptions.series>`
            property, that setting will be *overridden* by the contents of ``series``.

        :type kwargs: :class:`dict <python:dict>`

        :returns: A new :class:`Chart <highcharts_maps.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_maps.chart.Chart>`
        """
        kwargs = validators.dict(kwargs, allow_empty = True) or {}
        instance = cls(**kwargs)

        instance.add_series(series)

    @staticmethod
    def _get_options_obj(series_type, options_kwargs):
        """Return an :class:`Options` descendent based on the series type.

        :param series_type: Indicates the series type that should be created from the CSV
          data.
        :type series_type: :class:`str <python:str>`

        :param options_kwargs: A :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Options`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the CSV file instead.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: An :class:`Options` descendent.
        :rtype: :class:`HighchartsOptions` or :class:`HighchartsMapsOptions`
        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}

        if series_type not in MAPS_SERIES_LIST:
            options = HighchartsOptions(**options_kwargs)
        else:
            options = HighchartsMapsOptions(**options_kwargs)

        return options

    @classmethod
    def from_csv(cls,
                 as_string_or_file,
                 property_column_map = None,
                 series_type = 'line',
                 has_header_row = True,
                 series_kwargs = None,
                 options_kwargs = None,
                 chart_kwargs = None,
                 delimiter = ',',
                 null_text = 'None',
                 wrapper_character = "'",
                 line_terminator = '\r\n',
                 wrap_all_strings = False,
                 double_wrapper_character_when_nested = False,
                 escape_character = "\\",
                 is_maps_chart = False,
                 series_in_rows = False,
                 series_index = None,
                 **kwargs):
        """Create a new :class:`Chart <highcharts_core.chart.Chart>` instance with
        data populated from a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                my_chart = Chart.from_csv('some-csv-file.csv',
                                          property_column_map = {
                                              'x': 0,
                                              'y': 3,
                                              'id': 'id'
                                          },
                                          series_type = 'line')

            As the example above shows, data is loaded into the ``my_chart`` instance
            from the CSV file with a filename ``some-csv-file.csv``. The
            :meth:`x <CartesianData.x>`
            values for each data point will be taken from the first (index 0) column in
            the CSV file. The :meth:`y <CartesianData.y>` values will be taken from the
            fourth (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>`
            values will be taken from a column whose header row is labeled ``'id'``
            (regardless of its index).

        :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
          the raw CSV data as a :class:`str <python:str>` or a path to a file in the
          runtime environment that contains the CSV data.

          .. tip::

            Unwrapped empty column values are automatically interpreted as null
            (:obj:`None <python:None>`).

        :type as_string_or_file: :class:`str <python:str>` or Path-like

        :param property_column_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which CSV column. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value can either be a numerical index (starting with 0) or a
          :class:`str <python:str>` indicating the label for the CSV column. Defaults to
          :obj:`None <python:None>`.

          .. warning::

            If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
            file *must* have a header row (this is expected, by default). If there is no
            header row and a :class:`str <python:str>` value is found, a
            :exc:`HighchartsCSVDeserializationError` will be raised.

        :type property_column_map: :class:`dict <python:dict>`

        :param series_type: Indicates the series type that should be created from the CSV
          data.  Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param has_header_row: If ``True``, indicates that the first row of
          ``as_string_or_file`` contains column labels, rather than actual data. Defaults
          to ``True``.
        :type has_header_row: :class:`bool <python:bool>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from the CSV file instead.

        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the CSV file instead.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and CSV file instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce
            any value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\\\`` (which is Python for ``'\\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param is_maps_chart: If ``True``, indicates that the chart should be
          instantiated as a **Highcharts Maps for Python** chart. Defaults to ``False``.
        :type is_maps_chart: :class:`bool <python:bool>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to ``False``.
        :type series_in_rows: :class:`bool <python:bool>`

        :param series_index: If supplied, generate the chart with the series that 
          Highcharts for Python generated from ``df`` at the ``series_index`` position. 
          Defaults to :obj:`None <python:None>`, which includes all series generated 
          from ``df`` on the chart.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the CSV data.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        if not isinstance(options_kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'options_kwarts expects a dict. '
                                              f'Received: {options_kwargs.__class__.__name__}')
        if not options_kwargs:
            options_kwargs = {}

        if not isinstance(chart_kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'chart_kwargs expects a dict. '
                                              f'Received: {chart_kwargs.__class__.__name__}')
        if not chart_kwargs:
            chart_kwargs = {}

        if not isinstance(kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'kwargs expects a dict. '
                                              f'Received: {kwargs.__class__.__name__}')
        if not kwargs:
            kwargs = {}

        chart_kwargs['is_maps_chart'] = bool(is_maps_chart)

        series_cls = SERIES_CLASSES.get(series_type, None)

        if series_in_rows:
            series = series_cls.from_csv_in_rows(
                as_string_or_file,
                has_header_row = has_header_row,
                series_kwargs = series_kwargs,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = wrap_all_strings,
                double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                escape_character = escape_character,
                series_index = series_index,
                **kwargs
            )
        else:
            series = series_cls.from_csv(as_string_or_file,
                                         property_column_map = property_column_map,
                                         has_header_row = has_header_row,
                                         series_kwargs = series_kwargs,
                                         delimiter = delimiter,
                                         null_text = null_text,
                                         wrapper_character = wrapper_character,
                                         line_terminator = line_terminator,
                                         wrap_all_strings = wrap_all_strings,
                                         double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                                         escape_character = escape_character,
                                         series_index = series_index,
                                         **kwargs)

        if not isinstance(series, list):
            series = [series]

        options_kwargs['series'] = series

        options = cls._get_options_obj(series_type, options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_pandas(cls,
                    df,
                    property_map = None,
                    series_type = 'line',
                    series_kwargs = None,
                    options_kwargs = None,
                    chart_kwargs = None,
                    series_in_rows = False,
                    series_index = None,
                    **kwargs):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance whose
        data is populated from a `pandas <https://pandas.pydata.org/>`_
        :class:`DataFrame <pandas:pandas.DataFrame>`.

        :param df: The :class:`DataFrame <pandas:pandas.DataFrame>` from which data should be
          loaded.
        :type df: :class:`DataFrame <pandas:pandas.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pandas:pandas.DataFrame>` column. Defaults to 
          :obj:`None <python:None>`.
        :type property_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_type: Indicates the series type that should be created from the data
          in ``df``. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`
        
        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to 
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`

        :param series_index: If supplied, generate the chart with the series that 
          Highcharts for Python generated from ``df`` at the ``series_index`` position. 
          Defaults to :obj:`None <python:None>`, which includes all series generated 
          from ``df`` on the chart.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Additional keyword arguments that are - in turn - propagated to 
          the series created from the ``df``.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}
        kwargs = validators.dict(kwargs, allow_empty = True) or {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        if series_in_rows:
            series = series_cls.from_pandas_in_rows(df,
                                                    series_kwargs = series_kwargs,
                                                    series_index = series_index,
                                                    **kwargs)
        else:
            series = series_cls.from_pandas(df,
                                            property_map = property_map,
                                            series_kwargs = series_kwargs,
                                            series_index = series_index,
                                            **kwargs)

        if isinstance(series, series_cls):
            series = [series]

        options_kwargs['series'] = series
        options = cls._get_options_obj(series_type, options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_geopandas(cls,
                       gdf,
                       property_map = None,
                       series_type = 'line',
                       series_kwargs = None,
                       options_kwargs = None,
                       chart_kwargs = None,
                       series_in_rows = False,
                       series_index = None,
                       **kwargs):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance whose
        data is populated from a `geopandas <https://geopandas.org/>`__
        :class:`GeoDataFrame <geopandas:GeoDataFrame>`.

        :param gdf: The :class:`GeoDataFrame <geopandas:GeoDataFrame>` from which data
          should be loaded.
        :type gdf: :class:`GeoDataFrame <geopandas:GeoDataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``gdf``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`GeoDataFrame <geopandas:GeoDataFrame>` column. Defaults to 
          :obj:`None <python:None>`.
        :type property_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_type: Indicates the series type that should be created from the data
          in ``gdf``. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``gdf`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``gdf``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``gdf`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to 
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`
        
        :param series_index: If supplied, generate the chart with the series that 
          Highcharts for Python generated from ``df`` at the ``series_index`` position. 
          Defaults to :obj:`None <python:None>`, which includes all series generated 
          from ``df`` on the chart.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Additional keyword arguments that are - in turn - propagated to 
          the series created from the ``gdf``.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``gdf``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        if not series_type:
            raise errors.HighchartsValueError('series_type cannot be empty')
        series_type = str(series_type).lower()
        
        if not isinstance(options_kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'options_kwarts expects a dict. '
                                              f'Received: {options_kwargs.__class__.__name__}')
        if not options_kwargs:
            options_kwargs = {}

        if not isinstance(chart_kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'chart_kwargs expects a dict. '
                                              f'Received: {chart_kwargs.__class__.__name__}')
        if not chart_kwargs:
            chart_kwargs = {}

        if not isinstance(kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'kwargs expects a dict. '
                                              f'Received: {kwargs.__class__.__name__}')
        if not kwargs:
            kwargs = {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        if series_in_rows:
            series = series_cls.from_pandas_in_rows(gdf,
                                                    series_kwargs = series_kwargs,
                                                    series_index = series_index,
                                                    **kwargs)
        else:
            series = series_cls.from_pandas(gdf,
                                            property_map = property_map,
                                            series_kwargs = series_kwargs,
                                            series_index = series_index,
                                            **kwargs)

        if isinstance(series, series_cls):
            series = [series]

        options_kwargs['series'] = series
        options = cls._get_options_obj(series_type, options_kwargs)

        if not options.chart:
            options.chart = ChartOptions()

        options.chart.map = MapData.from_geodataframe(as_gdf = gdf)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_pyspark(cls,
                     df,
                     property_map,
                     series_type,
                     series_kwargs = None,
                     options_kwargs = None,
                     chart_kwargs = None):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance whose
        data is populated from a
        `PySpark <https://spark.apache.org/docs/latest/api/python/>`_
        :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`.

        :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
          should be loaded.
        :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` column.
        :type property_map: :class:`dict <python:dict>`

        :param series_type: Indicates the series type that should be created from the data
          in ``df``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsPySparkDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if
          `PySpark <https://spark.apache.org/docs/latest/api/python/>`_ is not available
          in the runtime environment
        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        options = cls._get_options_obj(series_type, options_kwargs)

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_pyspark(df,
                                         property_map,
                                         series_kwargs)

        options = HighchartsOptions(**options_kwargs)
        options.series = [series]

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_options(cls,
                     options,
                     chart_kwargs = None):
        """Create a :class:`Chart <highcharts_maps.chart.Chart>` instance from a
        :class:`HighchartsOptions <highcharts_maps.options.HighchartsOptions>` or
        :class:`HighchartsMapsOptions <highcharts_maps.options.HighchartsMapsOptions>`
        object.

        :param options: The configuration options to use to instantiate the chart.
        :type options:
          :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` or
          related or coercable

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the instance. Defaults to
          :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten* by the contents of ``options``.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: The :class:`Chart <highcharts_core.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}
        if checkers.is_type(options, 'HighchartsMapsOptions'):
            options = options
            chart_kwargs['is_maps_chart'] = True
        elif checkers.is_type(options, 'HighchartsOptions'):
            options = options
        elif ('mapNavigation' in options
              or 'map_navigation' in options
              or 'mapView' in options
              or 'map_view' in options):
            options = validate_types(options, HighchartsMapsOptions)
            chart_kwargs['is_maps_chart'] = True
        else:
            options = validate_types(options, HighchartsOptions)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @property
    def is_async(self) -> bool:
        """Read-only property which indicates whether the data visualization should be
        rendered using asynchronous logic.

        .. note::

          This property will only return ``True`` if one or more series rely on
          :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`

        :rtype: :class:`bool <python:bool>`
        """
        if not self.options or not self.options.series:
            return False

        if self.options.chart and hasattr(self.options.chart, 'is_async') and self.options.chart.is_async:
            return True

        for series in self.options.series:
            if hasattr(series, 'is_async') and series.is_async:
                return True

        return False

    @property
    def uses_custom_projection(self) -> bool:
        """Read-only property which indicates whether the map visualization applies a
        custom projection.

        .. note::

          This property will only return ``True`` if the
          ``options.map_views.projection.custom`` property is set.

        :rtype: :class:`bool <python:bool>`
        """
        if (not self.options
            or not hasattr(self.options, 'map_views')
            or not self.options.map_views
            or not self.options.map_views.projection):
            return False

        return self.options.map_views.projection.custom is not None

    def set_map_data(self, map_data):
        """Sets the default :term:`map geometries <map geometry>` for the chart.

        :param map_data: The :term:`map geometries <map geometry>` to set. Accepts:

          * :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
          * :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          * :class:`VariableName <highcharts_maps.utility_classes.javascript_functions.VariableName>`
          * :class:`GeoJSONBase <highcharts_maps.utility_classes.geojson.GeoJSONBase>` or
            descendant
          * :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>`
          * a :class:`str <python:str>` URL, which will be coerced to
            :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`

        :type map_data: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>` or
          :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          or :obj:`None <python:None>`
        """
        if self.options.chart:
            self.options.chart.map = map_data
        else:
            chart_options = ChartOptions(map = map_data)
            if self.options:
                self.options.chart = chart_options
            else:
                self.options = HighchartsMapsOptions(chart = chart_options)

    @classmethod
    def from_map_data(cls,
                      map_data,
                      options_kwargs = None,
                      chart_kwargs = None):
        """Create a :class:`Chart <highcharts_maps.chart.Chart>` instance from a
        :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>` or
        :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
        object.

        :param map_data: The :term:`map geometries <map geometry>` to set. Accepts:

          * :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
          * :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          * :class:`VariableName <highcharts_maps.utility_classes.javascript_functions.VariableName>`
          * :class:`GeoJSONBase <highcharts_maps.utility_classes.geojson.GeoJSONBase>` or
            descendant
          * :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>`
          * a :class:`str <python:str>` URL, which will be coerced to
            :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`

        :type map_data: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
          or :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          or :obj:`None <python:None>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instanting the options for the :class:`Chart`
          instance. Defaults to :obj:`None <python:None>`

          .. warning::

            If ``options_kwargs`` contains a ``chart.map`` setting, that value will
            be *overwritten* by the contents of ``map_data``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the instance. Defaults to
          :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` setting, that value will
            be *overwritten* by the options implied by ``options_kwargs``

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: The :class:`Chart <highcharts_core.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        """
        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        chart_kwargs['is_maps_chart'] = True
        options = HighchartsMapsOptions(**options_kwargs)
        if not options.chart:
            options.chart = ChartOptions()

        options.chart.map = map_data

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    def set_custom_projection(self, projection):
        """Applies a custom map :term:`projection` to the chart.

        :param projection: The custom :term:`projection` definition to apply.
        :type projection: :class:`CustomProjection <highcharts_maps.utility_classes.projections.CustomProjection>`

        .. seealso::

          * :ref:`Using Highcharts Maps for Python <using>` > :ref:`Using Custom Projections <custom_projections>`

        """
        projection = validate_types(projection, CustomProjection)

        if not self.options:
            self.options = HighchartsMapsOptions()

        if not self.options.map_view:
            self.options.map_view = MapViewOptions()

        if not self.options.map_view.projection:
            self.options.map_view.projection = ProjectionOptions()

        self.options.map_view.projection.custom = projection
