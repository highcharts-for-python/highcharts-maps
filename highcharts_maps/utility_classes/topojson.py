from typing import Optional
try:
    import orjson as json
except ImportError:
    try:
        import rapidjson as json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            import json

from validator_collection import validators, checkers

from topojson import Topology as TopologyBase


class Topology(TopologyBase):
    """Object representation of a :term:`topology`.

    .. note::

      Inherits from :class:`topojson.Topology <topojson:Topology>` with additional
      methods conforming to the
      :class:`HighchartsMeta <highcharts_maps.metaclasses.HighchartsMeta>` interface.

    """

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return as_dict

    @classmethod
    def from_dict(cls,
                  as_dict: dict,
                  allow_snake_case: bool = True):
        """Construct an instance of the class from a :class:`dict <python:dict>` object.

        :param as_dict: A :class:`dict <python:dict>` representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python object representation of ``as_dict``.
        :rtype: :class:`HighchartsMeta`
        """
        return cls(as_dict)

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return self.to_dict()

    def to_json(self,
                filename = None,
                encoding = 'utf-8'):
        """Generate a JSON string/byte string representation of the object compatible with
        the Highcharts JavaScript library.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A JSON representation of the object compatible with the Highcharts
          library.
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        if filename:
            filename = validators.path(filename)

        as_json = super().to_json()

        if filename:
            if isinstance(as_json, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_json)

        return as_json

    @classmethod
    def from_json(cls,
                  as_json_or_file: str | bytes,
                  allow_snake_case: bool = True):
        """Construct an instance of the class from a JSON string.

        :param as_json_or_file: The JSON string for the object or the filename of a file
          that contains the JSON string.
        :type as_jsonor_file: :class:`str <python:str>` or :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_json``.
        :rtype: :class:`MapData`
        """
        is_file = checkers.is_file(as_json_or_file)
        if is_file:
            with open(as_json_or_file, 'r') as file_:
                as_str = file_.read()
        else:
            as_str = as_json_or_file

        return cls.from_dict(as_str)

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

        as_str = self.to_json(encoding = encoding)

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    @classmethod
    def from_js_literal(cls,
                        as_str_or_file,
                        allow_snake_case: bool = True,
                        _break_loop_on_failure: bool = False):
        """Return a Python object representation of a Highcharts JavaScript object
        literal.

        :param as_str_or_file: The JavaScript object literal, represented either as a
          :class:`str <python:str>` or as a filename which contains the JS object literal.
        :type as_str_or_file: :class:`str <python:str>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :param _break_loop_on_failure: If ``True``, will break any looping operations in
          the event of a failure. Otherwise, will attempt to repair the failure. Defaults
          to ``False``.
        :type _break_loop_on_failure: :class:`bool <python:bool>`

        :returns: A Python object representation of the Highcharts JavaScript object
          literal.
        :rtype: :class:`HighchartsMeta`
        """
        return cls.from_json(as_str_or_file,
                             allow_snake_case = allow_snake_case)

    @classmethod
    def from_geojson(cls,
                     as_geojson_or_file: str | bytes,
                     allow_snake_case: bool = True,
                     **kwargs):
        """Construct an instance of the class from a JSON string.

        :param as_geojson_or_file: The :term:`GeoJSON` string for the object or the
          filename of a file that contains the GeoJSON string.
        :type as_geojson_or_file: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_geojson_or_file``.
        :rtype: :class:`MapData`
        """
        if checkers.is_file(as_geojson_or_file):
            with open(as_geojson_or_file, 'r') as file_:
                try:
                    as_dict = json.load(file_)
                except AttributeError:
                    as_str = file_.read()
                    as_dict = json.loads(as_str)
                obj = cls(as_dict, **kwargs)
        else:
            obj = cls(as_geojson_or_file, **kwargs)

        return obj

    @classmethod
    def from_topojson(cls,
                      as_topojson_or_file: str | bytes,
                      allow_snake_case: bool = True,
                      **kwargs):
        """Construct an instance of the class from a :term:`TopoJSON` string.

        :param as_topojson_or_file: The :term:`TopoJSON` string for the object or the
          filename of a file that contains the TopoJSON string.
        :type as_topojson_or_file: :class:`str <python:str>` or
          :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_topojson_or_file``.
        :rtype: :class:`MapData`
        """
        if checkers.is_file(as_topojson_or_file):
            with open(as_topojson_or_file, 'r') as file_:
                try:
                    as_dict = json.load(file_)
                except AttributeError:
                    as_str = file_.read()
                    as_dict = json.loads(as_str)
                obj = cls(as_dict, **kwargs)
        else:
            obj = cls(as_topojson_or_file, **kwargs)

        return obj

    def to_topojson(self,
                    filename = None,
                    encoding = 'utf-8'):
        """Generate a :term:`TopoJSON` string/byte string representation of the object.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A :term:`TopoJSON` representation of the object
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        return self.to_json(filename = filename, encoding = encoding)

    def to_geodataframe(self, object_name = None):
        """Generate a :class:`GeoPandas.GeoDataFrame <geopandas:GeoDataFrame>` instance
        of the :term:`topology`.

        :param object_name: If the map data contains multiple objects, you can generate
          serialize a specific object by specifying its name or index. Defaults to
          :obj:`None <python:None>`, which behaves as an index of 0.
        :type object_name: :class:`str <python:str>` or :class:`int <python:int>` or
          :obj:`None <python:None>`

        :rtype: :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`
        """
        return self.to_gdf(object_name = object_name)

    @classmethod
    def from_geodataframe(cls,
                          as_gdf,
                          prequantize = False,
                          **kwargs):
        """Create a :class:`MapData` instance from a
        :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`.

        :param as_gdf: The :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`
          containing the relevant :term:`map geometries <map geometry>`.
        :type as_gdf: :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`

        :param prequantize: If ``True``, will perform the TopoJSON optimizations
          ("quantizing the topology") before generating the :class:`Topology` instance.
          Defaults to ``False``.
        :type prequantize: :class:`bool <python:bool>`

        :rtype: :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
        """
        return cls(as_gdf, prequantize = prequantize, **kwargs)

    def to_svg(self, separate = False):
        """Display the arcs and junctions as SVG.

        :param separate: If ``True``, each of the arcs will be displayed separately.
          Defaults to ``False``.
        :type separate: :class:`bool <python:bool>`
        """
        super().to_svg(separate = separate)

    def to_gdf(self,
               crs = None,
               validate = False,
               winding_order = 'CCW_CW',
               object_name = 0):
        """Convert the Topology to a GeoDataFrame. Remember that this will destroy the
        computed Topology.

        .. note::

          This function does not use the TopoJSON driver within Fiona, but a custom
          implemented more robust variant. See for info the `to_geojson()` function.

        :param crs: coordinate reference system to set on the resulting frame. Default
          tries to use crs from data-input, otherwise is :obj:`None <python:None>`.
        :type crs: :class:`str <python:str>` or :class:`dict <python:dict>` or
          :obj:`None <python:None>`

        :param validate: Set to ``True`` to validate each feature before inclusion in the
          GeoJSON. Only features that are valid geometries objects will be included.
          Defaults to ``False``.
        :type validate: :class:`bool <python:bool>`

        :param winding_order:  Determines the winding order of the features in the output
          geometry. Accepts:

            * ``'CW_CCW'`` for clockwise orientation for outer rings  and
              counter-clockwise for interior rings
            * ``'CCW_CW'`` for counter-clockwise for outer rings and clockwise for
              interior rings.

          Default is `CCW_CW` for GeoJSON.
        :type winding_order: :class:`str <python:str>`

        :param object_name: Name or index of the object. Defaults to ``0`` to select the
          first object.
        :type object_name: :class:`str <python:str>` or :obj:`int <python:int>`

        :rtype: :class:`geopandas.GeoDataFrame <geopandas:GeoDataFrame>`
        """
        return super().to_gdf(crs = crs,
                              validate = validate,
                              winding_order = winding_order,
                              object_name = object_name)

    def to_alt(self,
               color = None,
               tooltip = True,
               projection = "identity",
               object_name = 0):
        """
        Display as Altair visualization.

        :param color: Assign a property attribute to be used for color encoding and
          renders the Altair visualization as geoshape. Remember that most of the time the
          wanted attribute is nested within properties. Moreover, specific type
          declaration is required. Eg ``color='properties.name:N'``. Defaults to
          :obj:`None <python:None>`, which renders as a mesh.
        :type color: :class:`str <python:str>` or :obj:`None <python:None>`

        :param tooltip: Option to include or exclude tooltips on geoshape objects.
          Defaults to ``True``.
        :type tooltip: :class:`bool <python:bool>`

        :param projection: Defines the projection of the visualization. Defaults to a
          non-geographic, Cartesian projection (known by Altair as ``'identity'``).
        :type projection: :class:`str <python:str>`

        :param object_name: The name or the index of the object within the Topology to
          display. Defaults to index ``0``.
        :type object_name: :class:`str <python:str>` or :class:`int <python:int>`
        """
        return super().to_alt(color = color,
                              tooltip = tooltip,
                              projection = projection,
                              object_name = object_name)

    def to_widget(self,
                  slider_toposimplify = None,
                  slider_topoquantize = None):
        """
        Create an interactive widget based on Altair. The widget includes sliders to
        interactively change the `toposimplify` and `topoquantize` settings.

        :param slider_toposimplify: A :class:`dict <python:dict>` which contains the
          keys: ``min``, ``max``, ``step``, ``value``. Defaults to:
          ``{"min": 0, "max": 10, "step": 0.01, "value": 0.01}``
        :type slider_toposimplify: :class:`dict <python:dict>`
        :param slider_topoquantize: A :class:`dict <python:dict>` which contains the keys:
          ``min``, ``max``, ``value``, ``base``. Defaults to:
          ``{"min": 1, "max": 6, "step": 1, "value": 1e5, "base": 10}``
        :type slider_topoquantize: :class:`dict <python:dict>`

        """
        if not slider_toposimplify:
            slider_toposimplify = {
                "min": 0,
                "max": 10,
                "step": 0.01,
                "value": 0.01
            }
        if not slider_topoquantize:
            slider_topoquantize = {
                "min": 1,
                "max": 6,
                "step": 1,
                "value": 1e5,
                "base": 10
            }

        super().to_widget(slider_toposimplify = slider_toposimplify,
                          slider_topoquantize = slider_topoquantize)

    def topoquantize(self, quant_factor, inplace = False):
        """Quantization is recommended to improve the quality of the topology if the
        input geometry is messy (i.e., small floating point error means that
        adjacent boundaries do not have identical values); typical values are powers
        of ten, such as ``1e4``, ``1e5``, or  ``1e6``.

        :param quant_factor: tolerance parameter
        :type quant_factor: :class:`float <python:float>`

        :param inplace: If ``True``, do operation in place and return
          :obj:`None <python:None>`. Defaults to ``False``.
        :type inplace: :class:`bool <python:bool>`

        :returns: Quantized coordinates and delta-encoded arcs if ``inplace`` is ``False``
        :rtype: object or :obj:`None <python:None>`
        """
        return super().topoquantize(quant_factor, inplace = inplace)

    def toposimplify(self,
                     epsilon,
                     simplify_algorithm = None,
                     simplify_with = None,
                     prevent_oversimplify = None,
                     inplace = False):
        """
        Apply toposimplify to remove unnecessary points from arcs after the topology
        is constructed. This will simplify the constructed arcs without altering the
        topological relations. Sensible values for coordinates stored in degrees are
        in the range of ``0.0001`` to ``10``.

        :param epsilon: tolerance parameter
        :type epsilon: :class:`float <python:float>`

        :param simplify_algorithm: Choose between ``'dp'`` and ``'vw'``, for
          Douglas-Peucker or Visvalingam-Whyatt respectively. ``'vw'`` will only be
          supported if ``simplify_with`` is set to ``'simplification'``. Defaults to
          :obj:`None <python:None>`, which behaves as ``'dp'``.
        :type simplify_algorithm: :class:`str <python:str>` or :obj:`None <python:None>`

        :param simplify_with: Sets the package to use for simplifying. Choose between
          ``'shapely'`` or ``'simplification'``. ``shapely`` only supports Douglas-Peucker
          and ``simplification`` supports both Douglas-Peucker and Visvalingam-Whyatt. The
          ``simplification`` package is known to be quicker than ``shapely``. Defaults to
          :obj:`None <python:None>`, which behaves as ``'shapely'``.
        :type simplify_with: :class:`str <python:str>` or :obj:`None <python:None>`

        :param prevent_oversimplify: If this setting is set to ``True``, the
          simplification is slower, but the likelihood of producing valid geometries is
          higher as it prevents oversimplification. Simplification happens on paths
          separately, so this setting is especially relevant for rings with no partial
          shared paths. This is also known as a topology-preserving variant of
          simplification. Defaults to :obj:`None <python:None>`, which behaves as
          ``True``.
        :type prevent_oversimplify: :class:`bool <python:bool>` or
          :obj:`None <python:None>`

        :param inplace: If ``True``, do operation in place and return
          :obj:`None <python:None>`. Defaults to ``False``.
        :type inplace: :class:`bool <python:bool>`

        :returns: Topology object with simplified linestrings if ``inplace`` is ``False``,
          otherwise :obj:`None <python:None>`
        :rtype: :class:`Topology <highcharts_maps.utility_classes.topojson.Topology>` or
          :obj:`None <python:None>`
        """
        return super().toposimplify(epsilon = epsilon,
                                    simplify_algorithm = simplify_algorithm,
                                    simplify_with = simplify_with,
                                    prevent_oversimplify = prevent_oversimplify,
                                    inplace = inplace)

    def to_dict(self, options = False):
        """Convert the Topology to a :class:`dict <python:dict>`.

        :param options: If ``True``, options also will be included. Defaults to ``False``.
        :type options: :class:`bool <python:bool>`

        :rtype: :class:`dict <python:dict>`
        """
        return super().to_dict(options = options)

    def to_geojson(self,
                   fp = None,
                   pretty = False,
                   indent = 4,
                   maxlinelength = 88,
                   validate = False,
                   winding_order = "CCW_CW",
                   decimals = None,
                   object_name = 0):
        """Convert the Topology to a :term:`GeoJSON` object. Remember that this will
        destroy the computed Topology.

        :param fp: If set, writes the object to a file on drive. Defaults to
          :obj:`None <python:None>`.
        :type fp: :class:`str <python:str>` or :obj:`None <python:None>`

        :param pretty: If ``True``, the JSON object will be 'pretty', depending on the
          ``ident`` and ``maxlinelength`` options. If ``False``, it will be compact,
          eliminating whitespace. Default is ``False``.
        :type pretty: :class:`bool <python:bool>`

        :param indent: If ``pretty`` is ``True``, determines object indentation. Defaults
          to ``4``.
        :type indent: :class:`int <python:int>`

        :param maxlinelength: If ``pretty`` is ``True``, determines the maximum length of
          each line. Defaults to ``88``.
        :type maxlinelength: :class:`int <python:int>`

        :param validate: Set to ``True`` to validate each feature before inclusion in the
          GeoJSON. Only features that are valid geometries objects will be included.
          Default is ``False``.
        :type validate: :class:`bool <python:bool>`

        :param winding_order:  Determines the winding order of the features in the output
          geometry. Accepts:

            * ``'CW_CCW'`` for clockwise orientation for outer rings  and
              counter-clockwise for interior rings
            * ``'CCW_CW'`` for counter-clockwise for outer rings and clockwise for
              interior rings.

          Default is `CCW_CW` for GeoJSON.
        :type winding_order: :class:`str <python:str>`

        :param decimals: Evenly round the coordinates to the given number of decimals.
            Default is :obj:`None <python:None>`, which means no rounding is applied.
        :type decimals: :class:`int <python:int>` or :obj:`None <python:None>`

        :param object_name: Name or index of the object. Defaults to ``0`` to select the
          first object.
        :type object_name: :class:`str <python:str>` or :obj:`int <python:int>`

        """
        return super().to_geojson(fp = fp,
                                  pretty = pretty,
                                  indent = indent,
                                  maxlinelength = maxlinelength,
                                  validate = validate,
                                  winding_order = winding_order,
                                  decimals = decimals,
                                  object_name = object_name)
