from typing import Optional, List

from validator_collection import validators, checkers

from highcharts_core.options.series.base import SeriesBase as CoreSeriesBase

from highcharts_maps import errors
from highcharts_maps.decorators import validate_types
from highcharts_maps.options.series.data.map_data import AsyncMapData, MapData
from highcharts_maps.utility_classes.javascript_functions import VariableName
from highcharts_maps.utility_functions import mro__to_untrimmed_dict
from highcharts_maps.js_literal_functions import (serialize_to_js_literal,
                                                  assemble_js_literal)


class SeriesBase(CoreSeriesBase):
    def convert_to(self, series_type):
        """Creates a new series of ``series_type`` from the current series.
        
        :param series_type: The series type that should be returned.
        :type series_type: :class:`str <python:str>` or
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descended
          
        .. warning::
        
          This operation is *not* guaranteed to work converting between all series 
          types. This is because some series types have different properties, different
          logic / functionality for their properties, and may have entirely different
          data requirements.
          
          In general, this method is expected to be *lossy* in nature, meaning that when
          the series can be converted "close enough" the series will be converted. 
          However, if the target ``series_type`` does not support certain properties set
          on the original instance, then those settings will *not* be propagated to the 
          new series.
          
          In certain cases, this method may raise an 
          :exc:`HighchartsSeriesConversionError <highcharts_core.errors.HighchartsSeriesConversionError>`
          if the method is unable to convert (even losing some data) the original into 
          ``series_type``.
        
        :returns: A new series of ``series_type``, maintaining relevant properties and
          data from the original instance.
        :rtype: ``series_type``
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>` descendant
          
        :raises HighchartsSeriesConversionError: if unable to convert (even after losing 
          some data) the original instance into an instance of ``series_type``.
        :raises HighchartsValueError: if ``series_type`` is not a recognized series type

        """
        from highcharts_maps.options.series.series_generator import SERIES_CLASSES

        if isinstance(series_type, str):
            series_type = series_type.lower()
            if series_type not in SERIES_CLASSES:
                raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                                  f'series type. Received: {series_type}')
            series_type_name = series_type
            series_type = SERIES_CLASSES.get(series_type)
        elif not issubclass(series_type, CoreSeriesBase):
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')
        else:
            series_type_name = series_type.__name__

        as_js_literal = self.to_js_literal()
        try:
            target = series_type.from_js_literal(as_js_literal)
        except (ValueError, TypeError):
            raise errors.HighchartsSeriesConversionError(f'Unable to convert '
                                                         f'{self.__class__.__name__} instance '
                                                         f'to {series_type_name}')
        
        return target


class MapSeriesBase(SeriesBase):
    """Generic base class for map series configurations."""

    def __init__(self, **kwargs):
        self._map_data = None

        self.map_data = kwargs.get('map_data', None)

        super().__init__(**kwargs)

    @property
    def map_data(self) -> Optional[MapData | AsyncMapData | VariableName | List[MapData | AsyncMapData]]:
        """:term:`Map geometries <map geometry>` that provide instructions on how to render
        the map itself, along with relevant properties used to join each map area to its
        corresponding values in the
        :meth:`.data <highcharts_maps.options.series.base.MapSeriesBase.data>`.

        Accepts (either in object representation or as coercable objects):

          * :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
          * :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          * :class:`VariableName <highcharts_maps.utility_classes.javascript_functions.VariableName>`
          * :class:`GeoJSONBase <highcharts_maps.utility_classes.geojson.GeoJSONBase>` or
            descendant
          * :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>`
          * a :class:`str <python:str>` URL, which will be coerced to
            :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>` or
          :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
          or :obj:`None <python:None>`
        """
        return self._map_data

    @map_data.setter
    def map_data(self, value):
        if not value:
            self._map_data = None
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
            cleaned_value = []
            for item in value:
                if isinstance(item, (MapData, AsyncMapData, VariableName)):
                    item = item
                elif checkers.is_url(item):
                    item = AsyncMapData(url = item)
                elif isinstance(item, dict) and 'url' in item:
                    item = AsyncMapData.from_dict(item)
                elif isinstance(item, str) and 'url:' in item:
                    item = AsyncMapData.from_json(item)
                elif checkers.is_type(item, 'GeoDataFrame'):
                    item = MapData.from_geodataframe(item)
                else:
                    try:
                        item = MapData.from_topojson(item)
                    except (ValueError, TypeError):
                        try:
                            item = MapData.from_geojson(item)
                        except (ValueError, TypeError):
                            raise errors.HighchartsValueError(
                                f'map_data expects a value '
                                f'that is TopoJSON, '
                                f'GeoJSON, a MapData '
                                f'object, an AsyncMapData '
                                f'object, or coercable to '
                                f'one. Received: '
                                f'{item.__class__.__name__}'
                            )
                cleaned_value.append(item)
            value = [x for x in cleaned_value]
        elif isinstance(value, (MapData, AsyncMapData)):
            value = value
        elif checkers.is_url(value):
            value = AsyncMapData(url = value)
        elif isinstance(value, dict) and 'url' in value:
            value = AsyncMapData.from_dict(value)
        elif isinstance(value, str) and 'url:' in value:
            value = AsyncMapData.from_json(value)
        elif checkers.is_type(value, 'GeoDataFrame'):
            value = MapData.from_geodataframe(value)
        else:
            try:
                value = MapData.from_topojson(value)
            except (ValueError, TypeError):
                try:
                    value = MapData.from_geojson(value)
                except (ValueError, TypeError):
                    try:
                        value = validate_types(value, VariableName)
                    except (ValueError, TypeError):
                        raise errors.HighchartsValueError(
                            f'map_data expects a value '
                            f'that is TopoJSON, '
                            f'GeoJSON, a MapData '
                            f'object, an AsyncMapData '
                            f'object, or coercable to '
                            f'one. Received: '
                            f'{value.__class__.__name__}'
                        )

        self._map_data = value

    def set_async_map_data(self,
                           url,
                           selector = None,
                           fetch_config = None):
        """Configures the asynchronous loading of :term:`map geometries <map geometry>`
        for the series, including a download of the raw map data itself in
        :term:`TopoJSON` or :term:`GeoJSON` format and the incorporation of an (optional)
        custom JavaScript function to select a portion of the downloaded data for
        rendering.

        :param url: The URL from which to retrieve the :term:`map geometry` asynchronously
          via a JavaScript ``fetch()`` call.
        :type url: :class:`str <python:str>`

        :param selector: A JavaScript callback function that the :term:`map geometry`
          retrieved from ``url`` will be supplied to, and which will then return a subset
          or mutated form of the resulting data. Defaults to :obj:`None <python:None>`.

          .. caution::

            The function *must* expect a single argument named ``originalMapData``.

        :type selector: :class:`CallbackFunction <highcharts_maps.utility_classes.javascript_functions.CallbackFunction>`

        :param fetch_config: Additional (optional) configuration settings to use for the
          JavaScript ``fetch()`` function call. Defaults to :obj:`None <python:None>`.

          .. note::

            If ``fetch_config`` contains an already-set URL, that URL will be
            overwritten by the value supplied in ``url``.

        :type fetch_config: :class:`FetchConfiguration <highcharts_maps.utility_classes.fetch_configuration.FetchConfiguration>`
          or :obj:`None <python:None>`
        """
        async_map_data = AsyncMapData(url = url,
                                      selector = selector,
                                      fetch_config = fetch_config)
        self.map_data = async_map_data

    @property
    def is_async(self) -> bool:
        """Read-only property, where ``True`` indicates that the map data is loaded
        asynchronously and ``False`` indicates that it is not.

        :rtype: :class:`bool <python:bool>`
        """
        if not self.map_data:
            return False
        is_async = isinstance(self.map_data, AsyncMapData)
        if is_async:
            return True
        if isinstance(self.map_data, list):
            for item in self.map_data:
                if isinstance(self.map_data, AsyncMapData):
                    return True

        return False

    @property
    def is_map_data_independent(self) -> bool:
        """Read-only property, where ``True`` indicates that the map data is referencing
        a JavaScript variable defined outside of **Highcharts Maps for Python**.

        :rtype: :class:`bool <python:bool>`
        """
        return isinstance(self.map_data, VariableName)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'inactive_other_points': as_dict.get('inactiveOtherPoints', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'map_data': as_dict.get('mapData', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'mapData': self.map_data,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

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

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self._to_untrimmed_dict()
        as_dict = {}
        for key in untrimmed:
            item = untrimmed[key]
            if key == 'mapData' and self.is_map_data_independent:
                item = f'HCP: REPLACE-WITH-{item.variable_name}'
            elif key == 'mapData' and self.is_async:
                fetch_counter = item.fetch_counter
                item = 'HCP: REPLACE-WITH-topology'
                if fetch_counter > 0:
                    item = f'{item}{fetch_counter}'

            serialized = serialize_to_js_literal(item,
                                                 encoding = encoding,
                                                 careful_validation = careful_validation)
            if serialized is not None:
                as_dict[key] = serialized

        as_str = assemble_js_literal(as_dict,
                                     careful_validation = careful_validation)

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    def load_from_geopandas(self,
                            gdf,
                            property_map):
        """Replace the contents of the
        :meth:`.data <highcharts_maps.options.series.base.SeriesBase.data>` property
        with data points and the
        :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>`
        property with geometries populated from a `geopandas <https://geopandas.org/>`__
        :class:`GeoDataFrame <geopandas:GeoDataFrame>`.

        :param gdf: The :class:`GeoDataFrame <geopandas:GeoDataFrame>` from which data
          should be loaded.
        :type gdf: :class:`GeoDataFrame <geopandas:GeoDataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``gdf``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`GeoDataFrame <geopandas:GeoDataFrame>` column.
        :type property_map: :class:`dict <python:dict>`

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `geopandas <https://geopandas.org/>`__ is
          not available in the runtime environment
        """
        self.map_data = MapData.from_geodataframe(as_gdf = gdf)

        try:
            from geopandas import GeoDataFrame
        except ImportError:
            raise errors.HighchartsDependencyError('geopandas is not available in the '
                                                   'runtime environment. Please install '
                                                   'using "pip install geopandas"')

        if not checkers.is_type(gdf, ('GeoDataFrame', 'Series')):
            raise errors.HighchartsValueError(f'gdf is expected to be a geopandas '
                                              f'GeoDataFrame or Series. Was: '
                                              f'{gdf.__class__.__name__}')

        self.map_data = MapData.from_geodataframe(as_gdf = gdf)
        self.load_from_pandas(gdf, property_map)

    @classmethod
    def from_geopandas(cls,
                       gdf,
                       property_map,
                       series_kwargs = None):
        """Create a :term:`series` instance whose
        :meth:`.data <highcharts_maps.options.series.base.SeriesBase.data>` property
        is populated from a `geopandas <https://geopandas.org/>`__
        :class:`GeoDataFrame <geopandas:GeoDataFrame>`.

        :param gdf: The :class:`GeoDataFrame <geopandas:GeoDataFrame>` from which data
          should be loaded.
        :type gdf: :class:`GeoDataFrame <geopandas:GeoDataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``gdf``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`GeoDataFrame <geopandas:GeoDataFrame>` column.
        :type property_map: :class:`dict <python:dict>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` or ``map_data`` key, their values
            will be *overwritten*. The ``data`` and ``map_data`` values will be created
            from ``gdf`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :returns: A :term:`series` instance (descended from
          :class:`MapSeriesBase <highcharts_maps.options.series.base.MapSeriesBase>`) with
          its :meth:`.data <highcharts_maps.options.series.base.SeriesBase.data>` and
          :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>`
          properties from the data in ``gdf```
        :rtype: :class:`list <python:list>` of series instances (descended from
          :class:`MapSeriesBase <highcharts_maps.options.series.base.MapSeriesBase>`)

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if
          `geopandas <https://geopandas.pydata.org/>`__ is not available in the runtime
          environment
        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        instance = cls(**series_kwargs)
        instance.load_from_geopandas(gdf, property_map)

        return instance

    def convert_to(self, series_type):
        """Creates a new series of ``series_type`` from the current series.
        
        :param series_type: The series type that should be returned.
        :type series_type: :class:`str <python:str>` or
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descended
          
        .. warning::
        
          This operation is *not* guaranteed to work converting between all series 
          types. This is because some series types have different properties, different
          logic / functionality for their properties, and may have entirely different
          data requirements.
          
          In general, this method is expected to be *lossy* in nature, meaning that when
          the series can be converted "close enough" the series will be converted. 
          However, if the target ``series_type`` does not support certain properties set
          on the original instance, then those settings will *not* be propagated to the 
          new series.
          
          In certain cases, this method may raise an 
          :exc:`HighchartsSeriesConversionError <highcharts_core.errors.HighchartsSeriesConversionError>`
          if the method is unable to convert (even losing some data) the original into 
          ``series_type``.
        
        :returns: A new series of ``series_type``, maintaining relevant properties and
          data from the original instance.
        :rtype: ``series_type``
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>` descendant
          
        :raises HighchartsSeriesConversionError: if unable to convert (even after losing 
          some data) the original instance into an instance of ``series_type``.
        :raises HighchartsValueError: if ``series_type`` is not a recognized series type

        """
        from highcharts_maps.options.series.series_generator import SERIES_CLASSES

        if isinstance(series_type, str):
            series_type = series_type.lower()
            if series_type not in SERIES_CLASSES:
                raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                                  f'series type. Received: {series_type}')
            series_type_name = series_type
            series_type = SERIES_CLASSES.get(series_type)
        elif not issubclass(series_type, CoreSeriesBase):
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')
        else:
            series_type_name = series_type.__name__

        as_js_literal = self.to_js_literal()
        try:
            target = series_type.from_js_literal(as_js_literal)
        except (ValueError, TypeError):
            raise errors.HighchartsSeriesConversionError(f'Unable to convert '
                                                         f'{self.__class__.__name__} instance '
                                                         f'to {series_type_name}')
        
        return target