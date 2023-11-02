##############################################################
:mod:`.options <highcharts_maps.options>`
##############################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  accessibility/index
  annotations/index
  axes/index
  boost
  caption
  chart/index
  credits
  data
  defs
  drilldown
  exporting/index
  legend/index
  loading
  map_navigation
  map_views/index
  navigation/index
  plot_options/index
  responsive
  series/index
  sonification/index
  subtitle
  time
  title
  tooltips

--------------

.. module:: highcharts_maps.options

****************************************************************************************
class: :class:`HighchartsMaOptions <highcharts_maps.options.HighchartsMapsOptions>`
****************************************************************************************

.. autoclass:: HighchartsMapsOptions
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMapsOptions
      :top-classes: highcharts_maps.metaclasses.HighchartsMeta, highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

-----------------------

****************************************************************************************
class: :class:`HighchartsOptions <highcharts_maps.options.HighchartsOptions>`
****************************************************************************************

.. autoclass:: HighchartsOptions
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsOptions
      :top-classes: highcharts_maps.metaclasses.HighchartsMeta, highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

-----------------------

****************************************************************************************
class: :class:`Options <highcharts_maps.options.Options>`
****************************************************************************************

.. autoclass:: Options
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: Options
      :top-classes: highcharts_maps.metaclasses.HighchartsMeta, highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

-----------------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.options <highcharts_maps.options>`
    - :class:`HighchartsMapsOptions <highcharts_maps.options.HighchartsMapsOptions>`
      :class:`HighchartsOptions <highcharts_maps.options.HighchartsOptions>`
      :class:`Options <highcharts_maps.options.Options>`
  * - :mod:`.options.accessibility <highcharts_maps.options.accessibility>`
    - :class:`Accessibility <highcharts_maps.options.accessibility.Accessibility>`
      :class:`CustomAccessibilityComponents <highcharts_maps.options.accessibility.CustomAccessibilityComponents>`
  * - :mod:`.options.accessibility.announce_new_data <highcharts_maps.options.accessibility.announce_new_data>`
    - :class:`AnnounceNewData <highcharts_maps.options.accessibility.announce_new_data.AnnounceNewData>`
  * - :mod:`.options.accessibility.keyboard_navigation <highcharts_maps.options.accessibility.keyboard_navigation>`
    - :class:`KeyboardNavigation <highcharts_maps.options.accessibility.keyboard_navigation.KeyboardNavigation>`
  * - :mod:`.options.accessibility.keyboard_navigation.focus_border <highcharts_maps.options.accessibility.keyboard_navigation.focus_border>`
    - :class:`FocusBorder <highcharts_maps.options.accessibility.keyboard_navigation.focus_border.FocusBorder>`
      :class:`FocusBorderStyle <highcharts_maps.options.accessibility.keyboard_navigation.focus_border.FocusBorderStyle>`
  * - :mod:`.options.accessibility.keyboard_navigation.series_navigation <highcharts_maps.options.accessibility.keyboard_navigation.series_navigation>`
    - :class:`SeriesNavigation <highcharts_maps.options.accessibility.keyboard_navigation.series_navigation.SeriesNavigation>`
  * - :mod:`options.accessibility.point <highcharts_maps.options.accessibility.point>`
    - :class:`AccessibilityPoint <highcharts_maps.options.accessibility.point.AccessibilityPoint>`
  * - :mod:`options.accessibility.screen_reader_section <highcharts_maps.options.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSection <highcharts_maps.options.accessibility.screen_reader_section.ScreenReaderSection>`
  * - :mod:`options.accessibility.series <highcharts_maps.options.accessibility.series>`
    - :class:`SeriesAccessibility <highcharts_maps.options.accessibility.series.SeriesAccessibility>`
  * - :mod:`.options.annotations <highcharts_maps.options.annotations>`
    - :class:`Annotation <highcharts_maps.options.annotations.Annotation>`
  * - :mod:`.options.annotations.animation <highcharts_maps.options.annotations.animation>`
    - :class:`AnnotationAnimation <highcharts_maps.options.annotations.animation.AnnotationAnimation>`
  * - :mod:`.options.annotations.control_point_options <highcharts_maps.options.annotations.control_point_options>`
    - :class:`AnnotationControlPointOption <highcharts_maps.options.annotations.control_point_options.AnnotationControlPointOption>`
  * - :mod:`.options.annotations.events <highcharts_maps.options.annotations.events>`
    - :class:`AnnotationEvent <highcharts_maps.options.annotations.events.AnnotationEvent>`
  * - :mod:`.options.annotations.label_options <highcharts_maps.options.annotations.label_options>`
    - :class:`AnnotationLabel <highcharts_maps.options.annotations.label_options.AnnotationLabel>`
      :class:`AnnotationLabelOptionAccessibility <highcharts_maps.options.annotations.label_options.AnnotationLabelOptionAccessibility>`
      :class:`LabelOptions <highcharts_maps.options.annotations.label_options.LabelOptions>`
  * - :mod:`.options.annotations.options.annotations.points <highcharts_maps.options.annotations.points>`
    - :class:`AnnotationPoint <highcharts_maps.options.annotations.points.AnnotationPoint>`
  * - :mod:`.options.annotations.shape_options <highcharts_maps.options.annotations.shape_options>`
    - :class:`AnnotationShape <highcharts_maps.options.annotations.shape_options.AnnotationShape>`
      :class:`ShapeOptions <highcharts_maps.options.annotations.shape_options.ShapeOptions>`
  * - :mod:`.options.axes <highcharts_maps.options.axes>`
    -
  * - :mod:`.options.axes.accessibility <highcharts_maps.options.axes.accessibility>`
    - :class:`AxisAccessibility <highcharts_maps.options.axes.accessibility.AxisAccessibility>`
  * - :mod:`.options.axes.breaks <highcharts_maps.options.axes.breaks>`
    - :class:`AxisBreak <highcharts_maps.options.axes.breaks.AxisBreak>`
  * - :mod:`.options.axes.color_axis <highcharts_maps.options.axes.color_axis>`
    - :class:`ColorAxis <highcharts_maps.options.axes.color_axis.ColorAxis>`
  * - :mod:`.options.axes.crosshair <highcharts_maps.options.axes.crosshair>`
    - :class:`CrosshairOptions <highcharts_maps.options.axes.crosshair.CrosshairOptions>`
  * - :mod:`.options.axes.data_classes <highcharts_maps.options.axes.data_classes>`
    - :class:`DataClass <highcharts_maps.options.axes.data_classes.DataClass>`
  * - :mod:`.options.axes.generic <highcharts_maps.options.axes.generic>`
    - :class:`GenericAxis <highcharts_maps.options.axes.generic.GenericAxis>`
  * - :mod:`.options.axes.labels <highcharts_maps.options.axes.labels>`
    - :class:`AxisLabelOptions <highcharts_maps.options.axes.labels.AxisLabelOptions>`
      :class:`PlotBandLabel <highcharts_maps.options.axes.labels.PlotBandLabel>`
      :class:`PlotLineLabel <highcharts_maps.options.axes.labels.PlotLineLabel>`
  * - :mod:`.options.axes.markers <highcharts_maps.options.axes.markers>`
    - :class:`AxisMarker <highcharts_maps.options.axes.markers.AxisMarker>`
  * - :mod:`.options.axes.numeric <highcharts_maps.options.axes.numeric>`
    - :class:`NumericAxis <highcharts_maps.options.axes.numeric.NumericAxis>`
  * - :mod:`.options.axes.parallel_axes <highcharts_maps.options.axes.parallel_axes>`
    - :class:`ParallelAxesOptions <highcharts_maps.options.axes.parallel_axes.ParallelAxesOptions>`
  * - :mod:`.options.axes.plot_bands <highcharts_maps.options.axes.plot_bands>`
    - :class:`PlotBand <highcharts_maps.options.axes.plot_bands.PlotBand>`
      :class:`PlotLine <highcharts_maps.options.axes.plot_bands.PlotLine>`
  * - :mod:`.options.axes.resize <highcharts_maps.options.axes.resize>`
    - :class:`ResizeOptions <highcharts_maps.options.axes.resize.ResizeOptions>`
      :class:`ControlledAxis <highcharts_maps.options.axes.resize.ControlledAxis>`
  * - :mod:`.options.axes.title <highcharts_maps.options.axes.title>`
    - :class:`AxisTitle <highcharts_maps.options.axes.title.AxisTitle>`
  * - :mod:`.options.axes.x_axis <highcharts_maps.options.axes.x_axis>`
    - :class:`XAxis <highcharts_maps.options.axes.x_axis.XAxis>`
  * - :mod:`.options.axes.y_axis <highcharts_maps.options.axes.y_axis>`
    - :class:`YAxis <highcharts_maps.options.axes.y_axis.YAxis>`
  * - :mod:`.options.axes.z_axis <highcharts_maps.options.axes.z_axis>`
    - :class:`ZAxis <highcharts_maps.options.axes.z_axis.ZAxis>`
  * - :mod:`.options.boost <highcharts_maps.options.boost>`
    - :class:`Boost <highcharts_maps.options.boost.Boost>`
      :class:`BoostDebug <highcharts_maps.options.boost.BoostDebug>`
  * - :mod:`.options.caption <highcharts_maps.options.caption>`
    - :class:`Caption <highcharts_maps.options.caption.Caption>`
  * - :mod:`.options.chart <highcharts_maps.options.chart>`
    - :class:`ChartOptions <highcharts_maps.options.chart.ChartOptions>`
      :class:`PanningOptions <highcharts_maps.options.chart.PanningOptions>`
  * - :mod:`.chart.options_3d <highcharts_maps.options.chart.options_3d>`
    - :class:`Options3D <highcharts_maps.options.chart.options_3d.Options3D>`
      :class:`Frame <highcharts_maps.options.chart.options_3d.Frame>`
      :class:`PanelOptions <highcharts_maps.options.chart.options_3d.PanelOptions>`
  * - :mod:`.chart.reset_zoom_button <highcharts_maps.options.chart.reset_zoom_button>`
    - :class:`ResetZoomButtonOptions <highcharts_maps.options.chart.reset_zoom_button.ResetZoomButtonOptions>`
  * - :mod:`.chart.scrollable_plot_area <highcharts_maps.options.chart.scrollable_plot_area>`
    - :class:`ScrollablePlotArea <highcharts_maps.options.chart.scrollable_plot_area.ScrollablePlotArea>`
  * - :mod:`.options.credits <highcharts_maps.options.credits>`
    - :class:`Credits <highcharts_maps.options.credits.Credits>`
      :class:`CreditStyleOptions <highcharts_maps.options.credits.CreditStyleOptions>`
  * - :mod:`.options.data <highcharts_maps.options.data>`
    - :class:`Data <highcharts_maps.options.data.Data>`
  * - :mod:`.options.defs <highcharts_maps.options.defs>`
    - :class:`MarkerDefinition <highcharts_maps.options.defs.MarkerDefinition>`
      :class:`MarkerASTNode <highcharts_maps.options.defs.MarkerASTNode>`
      :class:`MarkerAttributeObject <highcharts_maps.options.defs.MarkerAttributeObject>`
  * - :mod:`.options.drilldown <highcharts_maps.options.drilldown>`
    - :class:`Drilldown <highcharts_maps.options.drilldown.Drilldown>`
  * - :mod:`.options.exporting <highcharts_maps.options.exporting>`
    - :class:`Exporting <highcharts_maps.options.exporting.Exporting>`
      :class:`ExportingAccessibilityOptions <highcharts_maps.options.exporting.ExportingAccessibilityOptions>`
  * - :mod:`.options.exporting.csv <highcharts_maps.options.exporting.csv>`
    - :class:`ExportingCSV <highcharts_maps.options.exporting.csv.ExportingCSV>`
      :class:`CSVAnnotationOptions <highcharts_maps.options.exporting.csv.CSVAnnotationOptions>`
  * - :mod:`.options.exporting.exporting.pdf_font <highcharts_maps.options.exporting.pdf_font>`
    - :class:`PDFFontOptions <highcharts_maps.options.exporting.pdf_font.PDFFontOptions>`
  * - :mod:`.options.legend <highcharts_maps.options.legend>`
    - :class:`Legend <highcharts_maps.options.legend.Legend>`
  * - :mod:`.options.legend.accessibility <highcharts_maps.options.legend.accessibility>`
    - :class:`LegendAccessibilityOptions <highcharts_maps.options.legend.accessibility.LegendAccessibilityOptions>`
      :class:`LegendKeyboardNavigation <highcharts_maps.options.legend.accessibility.LegendKeyboardNavigation>`
  * - :mod:`.options.legend.bubble_legend <highcharts_maps.options.legend.bubble_legend>`
    - :class:`BubbleLegend <highcharts_maps.options.legend.bubble_legend.BubbleLegend>`
      :class:`BubbleLegendRange <highcharts_maps.options.legend.bubble_legend.BubbleLegendRange>`
      :class:`BubbleLegendLabelOptions <highcharts_maps.options.legend.bubble_legend.BubbleLegendLabelOptions>`
  * - :mod:`.options.legend.navigation <highcharts_maps.options.legend.navigation>`
    - :class:`LegendNavigation <highcharts_maps.options.legend.navigation.LegendNavigation>`
  * - :mod:`.options.legend.title <highcharts_maps.options.legend.title>`
    - :class:`LegendTitle <highcharts_maps.options.legend.title.LegendTitle>`
  * - :mod:`.options.loading <highcharts_maps.options.loading>`
    - :class:`Loading <highcharts_maps.options.loading.Loading>`
  * - :mod:`.options.map_navigation <highcharts_maps.options.map_navigation>`
    - :class:`MapNavigationOptions <highcharts_maps.options.map_navigation.MapNavigationOptions>`
      :class:`MapButtonOptions <highcharts_maps.options.map_navigation.MapButtonOptions>`
  * - :mod:`.options.map_views <highcharts_maps.options.map_views>`
    - :class:`MapViewOptions <highcharts_maps.options.map_views.MapViewOptions>`
  * - :mod:`.options.map_views.insets <highcharts_maps.options.map_views.insets>`
    - :class:`InsetOptions <highcharts_maps.options.map_views.insets.InsetOptions>`
      :class:`Inset <highcharts_maps.options.map_views.insets.Inset>`
  * - :mod:`.options.navigation <highcharts_maps.options.navigation>`
    - :class:`Navigation <highcharts_maps.options.navigation.Navigation>`
  * - :mod:`.options.navigation.bindings <highcharts_maps.options.navigation.bindings>`
    - :class:`Bindings <highcharts_maps.options.navigation.bindings.Bindings>`
      :class:`RectangleAnnotationBinding <highcharts_maps.options.navigation.bindings.RectangleAnnotationBinding>`
      :class:`LabelAnnotationBinding <highcharts_maps.options.navigation.bindings.LabelAnnotationBinding>`
      :class:`EllipseAnnotationBinding <highcharts_maps.options.navigation.bindings.EllipseAnnotationBinding>`
      :class:`CircleAnnotationBinding <highcharts_maps.options.navigation.bindings.CircleAnnotationBinding>`
      :class:`Binding <highcharts_maps.options.navigation.bindings.Binding>`
  * - :mod:`.options.plot_options <highcharts_maps.options.plot_options>`
    - :class:`PlotOptions <highcharts_maps.options.plot_options.PlotOptions>`
  * - :mod:`.options.plot_options.accessibility <highcharts_maps.options.plot_options.accessibility>`
    - :class:`TypeOptionsAccessibility <highcharts_maps.options.plot_options.accessibility.TypeOptionsAccessibility>`
      :class:`SeriesKeyboardNavigation <highcharts_maps.options.plot_options.accessibility.SeriesKeyboardNavigation>`
  * - :mod:`.options.plot_options.arcdiagram <highcharts_maps.options.plot_options.arcdiagram>`
    - :class:`ArcDiagramOptions <highcharts_maps.options.plot_options.arcdiagram.ArcDiagramOptions>`
  * - :mod:`.options.plot_options.area <highcharts_maps.options.plot_options.area>`
    - :class:`AreaOptions <highcharts_maps.options.plot_options.area.AreaOptions>`
      :class:`AreaRangeOptions <highcharts_maps.options.plot_options.area.AreaRangeOptions>`
      :class:`AreaSplineOptions <highcharts_maps.options.plot_options.area.AreaSplineOptions>`
      :class:`AreaSplineRangeOptions <highcharts_maps.options.plot_options.area.AreaSplineRangeOptions>`
      :class:`LineOptions <highcharts_maps.options.plot_options.area.LineOptions>`
      :class:`StreamGraphOptions <highcharts_maps.options.plot_options.area.StreamGraphOptions>`
  * - :mod:`.options.plot_options.bar <highcharts_maps.options.plot_options.bar>`
    - :class:`BarOptions <highcharts_maps.options.plot_options.bar.BarOptions>`
      :class:`ColumnOptions <highcharts_maps.options.plot_options.bar.ColumnOptions>`
      :class:`ColumnPyramidOptions <highcharts_maps.options.plot_options.bar.ColumnPyramidOptions>`
      :class:`ColumnRangeOptions <highcharts_maps.options.plot_options.bar.ColumnRangeOptions>`
      :class:`CylinderOptions <highcharts_maps.options.plot_options.bar.CylinderOptions>`
      :class:`VariwideOptions <highcharts_maps.options.plot_options.bar.VariwideOptions>`
      :class:`WaterfallOptions <highcharts_maps.options.plot_options.bar.WaterfallOptions>`
      :class:`WindBarbOptions <highcharts_maps.options.plot_options.bar.WindBarbOptions>`
      :class:`XRangeOptions <highcharts_maps.options.plot_options.bar.XRangeOptions>`
      :class:`BaseBarOptions <highcharts_maps.options.plot_options.bar.BaseBarOptions>`
  * - :mod:`.options.plot_options.base <highcharts_maps.options.plot_options.base>`
    - :class:`MapBaseOptions <highcharts_maps.options.plot_options.base.MapBaseOptions>`
  * - :mod:`.options.plot_options.bellcurve <highcharts_maps.options.plot_options.bellcurve>`
    - :class:`BellCurveOptions <highcharts_maps.options.plot_options.bellcurve.BellCurveOptions>`
  * - :mod:`.options.plot_options.boxplot <highcharts_maps.options.plot_options.boxplot>`
    - :class:`BoxPlotOptions <highcharts_maps.options.plot_options.boxplot.BoxPlotOptions>`
      :class:`ErrorBarOptions <highcharts_maps.options.plot_options.boxplot.ErrorBarOptions>`
  * - :mod:`.options.plot_options.bubble <highcharts_maps.options.plot_options.bubble>`
    - :class:`BubbleOptions <highcharts_maps.options.plot_options.bubble.BubbleOptions>`
  * - :mod:`.options.plot_options.bullet <highcharts_maps.options.plot_options.bullet>`
    - :class:`BulletOptions <highcharts_maps.options.plot_options.bullet.BulletOptions>`
      :class:`TargetOptions <highcharts_maps.options.plot_options.bullet.TargetOptions>`
  * - :mod:`.options.plot_options.data_sorting <highcharts_maps.options.plot_options.data_sorting>`
    - :class:`DataSorting <highcharts_maps.options.plot_options.data_sorting.DataSorting>`
  * - :mod:`.options.plot_options.dependencywheel <highcharts_maps.options.plot_options.dependencywheel>`
    - :class:`DependencyWheelOptions <highcharts_maps.options.plot_options.dependencywheel.DependencyWheelOptions>`
  * - :mod:`.options.plot_options.drag_drop <highcharts_maps.options.plot_options.drag_drop>`
    - :class:`DragDropOptions <highcharts_maps.options.plot_options.drag_drop.DragDropOptions>`
      :class:`HighLowDragDropOptions <highcharts_maps.options.plot_options.drag_drop.HighLowDragDropOptions>`
      :class:`BoxPlotDragDropOptions <highcharts_maps.options.plot_options.drag_drop.BoxPlotDragDropOptions>`
      :class:`BulletDragDropOptions <highcharts_maps.options.plot_options.drag_drop.BulletDragDropOptions>`
      :class:`GuideBox <highcharts_maps.options.plot_options.drag_drop.GuideBox>`
      :class:`GuideBoxOptions <highcharts_maps.options.plot_options.drag_drop.GuideBoxOptions>`
      :class:`DragHandle <highcharts_maps.options.plot_options.drag_drop.DragHandle>`
  * - :mod:`.options.plot_options.dumbbell <highcharts_maps.options.plot_options.dumbbell>`
    - :class:`DumbbellOptions <highcharts_maps.options.plot_options.dumbbell.DumbbellOptions>`
      :class:`LollipopOptions <highcharts_maps.options.plot_options.dumbbell.LollipopOptions>`
  * - :mod:`.options.plot_options.flowmap <highcharts_maps.options.plot_options.flowmap>`
    - :class:`FlowmapOptions <highcharts_maps.options.plot_options.flowmap.FlowmapOptions>`
      :class:`GeoHeatmapOptions <highcharts_maps.options.plot_options.flowmap.GeoHeatmapOptions>`
      :class:`InterpolationOptions <highcharts_maps.options.plot_options.flowmap.InterpolationOptions>`
  * - :mod:`.options.plot_options.funnel <highcharts_maps.options.plot_options.funnel>`
    - :class:`FunnelOptions <highcharts_maps.options.plot_options.funnel.FunnelOptions>`
      :class:`Funnel3DOptions <highcharts_maps.options.plot_options.funnel.Funnel3DOptions>`
  * - :mod:`.options.plot_options.gauge <highcharts_maps.options.plot_options.gauge>`
    - :class:`GaugeOptions <highcharts_maps.options.plot_options.gauge.GaugeOptions>`
      :class:`SolidGaugeOptions <highcharts_maps.options.plot_options.gauge.SolidGaugeOptions>`
  * - :mod:`.options.plot_options.generic <highcharts_maps.options.plot_options.generic>`
    - :class:`GenericTypeOptions <highcharts_maps.options.plot_options.generic.GenericTypeOptions>`
  * - :mod:`.options.plot_options.heatmap <highcharts_maps.options.plot_options.heatmap>`
    - :class:`HeatmapOptions <highcharts_maps.options.plot_options.heatmap.HeatmapOptions>`
      :class:`TilemapOptions <highcharts_maps.options.plot_options.heatmap.TilemapOptions>`
  * - :mod:`.options.plot_options.histogram <highcharts_maps.options.plot_options.histogram>`
    - :class:`HistogramOptions <highcharts_maps.options.plot_options.histogram.HistogramOptions>`
  * - :mod:`.options.plot_options.item <highcharts_maps.options.plot_options.item>`
    - :class:`ItemOptions <highcharts_maps.options.plot_options.item.ItemOptions>`
  * - :mod:`.options.plot_options.levels <highcharts_maps.options.plot_options.levels>`
    - :class:`LevelOptions <highcharts_maps.options.plot_options.levels.LevelOptions>`
      :class:`SunburstLevelOptions <highcharts_maps.options.plot_options.levels.SunburstLevelOptions>`
      :class:`TreemapLevelOptions <highcharts_maps.options.plot_options.levels.TreemapLevelOptions>`
      :class:`LevelSize <highcharts_maps.options.plot_options.levels.LevelSize>`
      :class:`ColorVariation <highcharts_maps.options.plot_options.levels.ColorVariation>`
      :class:`BaseLevelOptions <highcharts_maps.options.plot_options.levels.BaseLevelOptions>`
  * - :mod:`.options.plot_options.link <highcharts_maps.options.plot_options.link>`
    - :class:`LinkOptions <highcharts_maps.options.plot_options.link.LinkOptions>`
  * - :mod:`.options.plot_options.map <highcharts_maps.options.plot_options.map>`
    - :class:`MapOptions <highcharts_maps.options.plot_options.map.MapOptions>`
  * - :mod:`.options.plot_options.mapbubble <highcharts_maps.options.plot_options.mapbubble>`
    - :class:`MapBubbleOptions <highcharts_maps.options.plot_options.mapbubble.MapBubbleOptions>`
  * - :mod:`.options.plot_options.mapline <highcharts_maps.options.plot_options.mapline>`
    - :class:`MapLineOptions <highcharts_maplines.options.plot_options.mapline.MapLineOptions>`
  * - :mod:`.options.plot_options.mappoint <highcharts_maps.options.plot_options.mappoint>`
    - :class:`MapPointOptions <highcharts_maps.options.plot_options.mappoint.MapPointOptions>`
  * - :mod:`.options.plot_options.networkgraph <highcharts_maps.options.plot_options.networkgraph>`
    - :class:`NetworkGraphOptions <highcharts_maps.options.plot_options.networkgraph.NetworkGraphOptions>`
      :class:`LayoutAlgorithm <highcharts_maps.options.plot_options.networkgraph.LayoutAlgorithm>`
  * - :mod:`.options.plot_options.organization <highcharts_maps.options.plot_options.organization>`
    - :class:`OrganizationOptions <highcharts_maps.options.plot_options.organization.OrganizationOptions>`
  * - :mod:`.options.plot_options.packedbubble <highcharts_maps.options.plot_options.packedbubble>`
    - :class:`PackedBubbleOptions <highcharts_maps.options.plot_options.packedbubble.PackedBubbleOptions>`
      :class:`ParentNodeOptions <highcharts_maps.options.plot_options.packedbubble.ParentNodeOptions>`
  * - :mod:`.options.plot_options.pareto <highcharts_maps.options.plot_options.pareto>`
    - :class:`ParetoOptions <highcharts_maps.options.plot_options.pareto.ParetoOptions>`
  * - :mod:`.options.plot_options.pictorial <highcharts_maps.options.plot_options.pictorial>`
    - :class:`PictorialOptions <highcharts_maps.options.plot_options.pictorial.PictorialOptions>`
  * - :mod:`.options.plot_options.pie <highcharts_maps.options.plot_options.pie>`
    - :class:`PieOptions <highcharts_maps.options.plot_options.pie.PieOptions>`
      :class:`VariablePieOptions <highcharts_maps.options.plot_options.pie.VariablePieOptions>`
  * - :mod:`.options.plot_options.points <highcharts_maps.options.plot_options.points>`
    - :class:`Point <highcharts_maps.options.plot_options.points.Point>`
      :class:`OnPointOptions <highcharts_maps.options.plot_options.points.OnPointOptions>`
      :class:`ConnectorOptions <highcharts_maps.options.plot_options.points.ConnectorOptions>`
  * - :mod:`.options.plot_options.polygon <highcharts_maps.options.plot_options.polygon>`
    - :class:`PolygonOptions <highcharts_maps.options.plot_options.polygon.PolygonOptions>`
  * - :mod:`.options.plot_options.pyramid <highcharts_maps.options.plot_options.pyramid>`
    - :class:`PyramidOptions <highcharts_maps.options.plot_options.pyramid.PyramidOptions>`
      :class:`Pyramid3DOptions <highcharts_maps.options.plot_options.pyramid.Pyramid3DOptions>`
  * - :mod:`.options.plot_options.sankey <highcharts_maps.options.plot_options.sankey>`
    - :class:`SankeyOptions <highcharts_maps.options.plot_options.sankey.SankeyOptions>`
  * - :mod:`.options.plot_options.scatter <highcharts_maps.options.plot_options.scatter>`
    - :class:`ScatterOptions <highcharts_maps.options.plot_options.scatter.ScatterOptions>`
      :class:`Scatter3DOptions <highcharts_maps.options.plot_options.scatter.Scatter3DOptions>`
  * - :mod:`.options.plot_options.series <highcharts_maps.options.plot_options.series>`
    - :class:`SeriesOptions <highcharts_maps.options.plot_options.series.SeriesOptions>`
  * - :mod:`.options.plot_options.sonification <highcharts_maps.options.plot_options.sonification>`
    - :class:`SeriesSonification <highcharts_maps.options.plot_options.sonification.SeriesSonification>`
  * - :mod:`.options.plot_options.spline <highcharts_maps.options.plot_options.spline>`
    - :class:`SplineOptions <highcharts_maps.options.plot_options.spline.SplineOptions>`
  * - :mod:`.options.plot_options.sunburst <highcharts_maps.options.plot_options.sunburst>`
    - :class:`SunburstOptions <highcharts_maps.options.plot_options.sunburst.SunburstOptions>`
  * - :mod:`.options.plot_options.tiledwebmap <highcharts_maps.options.plot_options.tiledwebmap'>`
    - :class:`TiledWebMapOptions <highcharts_maps.options.plot_options.tiledwebmap.TiledWebMapOptions>`
      :class:`ProviderOptions <highcharts_maps.options.plot_options.tiledwebmap.ProviderOptions>`
  * - :mod:`.options.plot_options.timeline <highcharts_maps.options.plot_options.timeline>`
    - :class:`TimelineOptions <highcharts_maps.options.plot_options.timeline.TimelineOptions>`
  * - :mod:`.options.plot_options.treegraph <highcharts_maps.options.plot_options.treegraph>`
    - :class:`TreegraphOptions <highcharts_maps.options.plot_options.treegraph.TreegraphOptions>`
      :class:`TreegraphEvents <highcharts_maps.options.plot_options.treegraph.TreegraphEvents>`
  * - :mod:`.options.plot_options.treemap <highcharts_maps.options.plot_options.treemap>`
    - :class:`TreemapOptions <highcharts_maps.options.plot_options.treemap.TreemapOptions>`
  * - :mod:`.options.plot_options.vector <highcharts_maps.options.plot_options.vector>`
    - :class:`VectorOptions <highcharts_maps.options.plot_options.vector.VectorOptions>`
  * - :mod:`.options.plot_options.venn <highcharts_maps.options.plot_options.venn>`
    - :class:`VennOptions <highcharts_maps.options.plot_options.venn.VennOptions>`
  * - :mod:`.options.plot_options.wordcloud <highcharts_maps.options.plot_options.wordcloud>`
    - :class:`WordcloudOptions <highcharts_maps.options.plot_options.wordcloud.WordcloudOptions>`
      :class:`RotationOptions <highcharts_maps.options.plot_options.wordcloud.RotationOptions>`
  * - :mod:`.options.responsive <highcharts_maps.options.responsive>`
    - :class:`Responsive <highcharts_maps.options.responsive.Responsive>`
      :class:`ResponsiveRules <highcharts_maps.options.responsive.ResponsiveRules>`
      :class:`Condition <highcharts_maps.options.responsive.Condition>`
  * - :mod:`.options.series <highcharts_maps.options.series>`
    -
  * - :mod:`.options.series.arcdiagram <highcharts_maps.options.series.arcdiagram>`
    - :class:`ArcDiagramSeries <highcharts_maps.options.series.arcdiagram.ArcDiagramSeries>`
  * - :mod:`.options.series.area <highcharts_maps.options.series.area>`
    - :class:`AreaSeries <highcharts_maps.options.series.area.AreaSeries>`
      :class:`AreaRangeSeries <highcharts_maps.options.series.area.AreaRangeSeries>`
      :class:`AreaSplineSeries <highcharts_maps.options.series.area.AreaSplineSeries>`
      :class:`AreaSplineRangeSeries <highcharts_maps.options.series.area.AreaSplineRangeSeries>`
      :class:`LineSeries <highcharts_maps.options.series.area.LineSeries>`
      :class:`StreamGraphSeries <highcharts_maps.options.series.area.StreamGraphSeries>`
  * - :mod:`.options.series.bar <highcharts_maps.options.series.bar>`
    - :class:`BarSeries <highcharts_maps.options.series.bar.BarSeries>`
      :class:`ColumnSeries <highcharts_maps.options.series.bar.ColumnSeries>`
      :class:`ColumnPyramidSeries <highcharts_maps.options.series.bar.ColumnPyramidSeries>`
      :class:`ColumnRangeSeries <highcharts_maps.options.series.bar.ColumnRangeSeries>`
      :class:`CylinderSeries <highcharts_maps.options.series.bar.CylinderSeries>`
      :class:`VariwideSeries <highcharts_maps.options.series.bar.VariwideSeries>`
      :class:`WaterfallSeries <highcharts_maps.options.series.bar.WaterfallSeries>`
      :class:`WindBarbSeries <highcharts_maps.options.series.bar.WindBarbSeries>`
      :class:`XRangeSeries <highcharts_maps.options.series.bar.XRangeSeries>`
      :class:`BaseBarSeries <highcharts_maps.options.series.bar.BaseBarSeries>`
  * - :mod:`.options.series.base <highcharts_maps.options.series.base>`
    - :class:`MapSeriesBase <highcharts_maps.options.series.base.MapSeriesBase>`
      :class:`SeriesBase <highcharts_maps.options.series.base.SeriesBase>`
  * - :mod:`.options.series.bellcurve <highcharts_maps.options.series.bellcurve>`
    - :class:`BellCurveSeries <highcharts_maps.options.series.bellcurve.BellCurveSeries>`
  * - :mod:`.options.series.boxplot <highcharts_maps.options.series.boxplot>`
    - :class:`BoxPlotSeries <highcharts_maps.options.series.boxplot.BoxPlotSeries>`
      :class:`ErrorBarSeries <highcharts_maps.options.series.boxplot.ErrorBarSeries>`
  * - :mod:`.options.series.bubble <highcharts_maps.options.series.bubble>`
    - :class:`BubbleSeries <highcharts_maps.options.series.bubble.BubbleSeries>`
  * - :mod:`.options.series.bullet <highcharts_maps.options.series.bullet>`
    - :class:`BulletSeries <highcharts_maps.options.series.bullet.BulletSeries>`
  * - :mod:`.options.series.data <highcharts_maps.options.series.data>`
    -
  * - :mod:`.options.series.data.accessibility <highcharts_maps.options.series.data.accessibility>`
    - :class:`DataPointAccessibility <highcharts_maps.options.series.data.accessibility.DataPointAccessibility>`
  * - :mod:`.options.series.data.arcdiagram <highcharts_maps.options.series.data.arcdiagram>`
    - :class:`ArcDiagramData <highcharts_maps.options.series.data.arcdiagram.ArcDiagramData>`
  * - :mod:`.options.series.data.bar <highcharts_maps.options.series.data.bar>`
    - :class:`BarData <highcharts_maps.options.series.data.bar.BarData>`
      :class:`WaterfallData <highcharts_maps.options.series.data.bar.WaterfallData>`
      :class:`WindBarbData <highcharts_maps.options.series.data.bar.WindBarbData>`
      :class:`XRangeData <highcharts_maps.options.series.data.bar.XRangeData>`
  * - :mod:`.options.series.data.base <highcharts_maps.options.series.data.base>`
    - :class:`DataBase <highcharts_maps.options.series.data.base.DataBase>`
      :class:`DataCore <highcharts_maps.options.series.data.base.DataCore>`
  * - :mod:`.options.series.data.boxplot <highcharts_maps.options.series.data.boxplot>`
    - :class:`BoxPlotData <highcharts_maps.options.series.data.boxplot.BoxPlotData>`
  * - :mod:`.options.series.data.bullet <highcharts_maps.options.series.data.bullet>`
    - :class:`BulletData <highcharts_maps.options.series.data.bullet.BulletData>`
  * - :mod:`.options.series.data.cartesian <highcharts_maps.options.series.data.cartesian>`
    - :class:`CartesianData <highcharts_maps.options.series.data.cartesian.CartesianData>`
      :class:`Cartesian3DData <highcharts_maps.options.series.data.cartesian.Cartesian3DData>`
      :class:`CartesianValueData <highcharts_maps.options.series.data.cartesian.CartesianValueData>`
  * - :mod:`.options.series.data.connections <highcharts_maps.options.series.data.connections>`
    - :class:`ConnectionData <highcharts_maps.options.series.data.connections.ConnectionData>`
      :class:`FlowmapData <highcharts_maps.options.series.data.connections.FlowmapData>`
      :class:`WeightedConnectionData <highcharts_maps.options.series.data.connections.WeightedConnectionData>`
      :class:`OutgoingWeightedConnectionData <highcharts_maps.options.series.data.connections.OutgoingWeightedConnectionData>`
      :class:`ConnectionBase <highcharts_maps.options.series.data.connections.ConnectionBase>`
  * - :mod:`.options.series.data.geometric <highcharts_maps.options.series.data.geometric>`
    - :class:`GeometricData <highcharts_maps.options.series.data.GeometricData`
      :class:`GeometricZData <highcharts_maps.options.series.data.GeometricZData`
      :class:`GeometricLatLonData <highcharts_maps.options.series.data.GeometricLatLonData`
      :class:`GeometricDataBase <highcharts_maps.options.series.data.GeometricDataBase`
  * - :mod:`.options.series.data.map_data <highcharts_maps.options.series.data.map_data>`
    - :class:`MapData <highcharts_maps.options.series.data.map_data.MapData>`
      :class:`AsyncMapData <highcharts_maps.options.series.data.map_data.AsyncMapData>`
  * - :mod:`.options.series.data.pie <highcharts_maps.options.series.data.pie>`
    - :class:`PieData <highcharts_maps.options.series.data.pie.PieData>`
      :class:`VariablePieData <highcharts_maps.options.series.data.pie.VariablePieData>`
  * - :mod:`.options.series.data.range <highcharts_maps.options.series.data.range>`
    - :class:`RangeData <highcharts_maps.options.series.data.range.RangeData>`
      :class:`ConnectedRangeData <highcharts_maps.options.series.data.range.ConnectedRangeData>`
  * - :mod:`.options.series.data.single_point <highcharts_maps.options.series.data.single_point>`
    - :class:`SinglePointData <highcharts_maps.options.series.data.single_point.SinglePointData>`
      :class:`SingleValueData <highcharts_maps.options.series.data.single_point.SingleValueData>`
      :class:`SingleXData <highcharts_maps.options.series.data.single_point.SingleXData>`
      :class:`LabeledSingleXData <highcharts_maps.options.series.data.single_point.LabeledSingleXData>`
      :class:`ConnectedSingleXData <highcharts_maps.options.series.data.single_point.ConnectedSingleXData>`
      :class:`SinglePointBase <highcharts_maps.options.series.data.single_point.SinglePointBase>`
  * - :mod:`.options.series.data.sunburst <highcharts_maps.options.series.data.sunburst>`
    - :class:`SunburstData <highcharts_maps.options.series.data.sunburst.SunburstData>`
  * - :mod:`.options.series.data.treegraph <highcharts_maps.options.series.data.treegraph>`
    - :class:`TreegraphData <highcharts_maps.options.series.data.treegraph.TreegraphData>`
  * - :mod:`.options.series.data.treemap <highcharts_maps.options.series.data.treemap>`
    - :class:`TreemapData <highcharts_maps.options.series.data.treemap.TreemapData>`
  * - :mod:`.options.series.data.vector <highcharts_maps.options.series.data.vector>`
    - :class:`VectorData <highcharts_maps.options.series.data.vector.VectorData>`
  * - :mod:`.options.series.data.venn <highcharts_maps.options.series.data.venn>`
    - :class:`VennData <highcharts_maps.options.series.data.venn.VennData>`
  * - :mod:`.options.series.data.wordcloud <highcharts_maps.options.series.data.wordcloud>`
    - :class:`WordcloudData <highcharts_maps.options.series.data.wordcloud.WordcloudData>`
  * - :mod:`.options.series.dependencywheel <highcharts_maps.options.series.dependencywheel>`
    - :class:`DependencyWheelSeries <highcharts_maps.options.series.dependencywheel.DependencyWheelSeries>`
  * - :mod:`.options.series.dumbbell <highcharts_maps.options.series.dumbbell>`
    - :class:`DumbbellSeries <highcharts_maps.options.series.dumbbell.DumbbellSeries>`
      :class:`LollipopSeries <highcharts_maps.options.series.dumbbell.LollipopSeries>`
  * - :mod:`.options.series.flowmap <highcharts_maps.options.series.flowmap>`
    - :class:`FlowmapSeries <highcharts_maps.options.series.flowmap.FlowmapSeries>`
      :class:`GeoHeatmapSeries <highcharts_maps.options.series.flowmap.GeoHeatmapSeries>`
  * - :mod:`.options.series.funnel <highcharts_maps.options.series.funnel>`
    - :class:`FunnelSeries <highcharts_maps.options.series.funnel.FunnelSeries>`
      :class:`Funnel3DSeries <highcharts_maps.options.series.funnel.Funnel3DSeries>`
  * - :mod:`.options.series.gauge <highcharts_maps.options.series.gauge>`
    - :class:`GaugeSeries <highcharts_maps.options.series.gauge.GaugeSeries>`
      :class:`SolidGaugeSeries <highcharts_maps.options.series.gauge.SolidGaugeSeries>`
  * - :mod:`.options.series.heatmap <highcharts_maps.options.series.heatmap>`
    - :class:`HeatmapSeries <highcharts_maps.options.series.heatmap.HeatmapSeries>`
      :class:`TilemapSeries <highcharts_maps.options.series.heatmap.TilemapSeries>`
  * - :mod:`.options.series.histogram <highcharts_maps.options.series.histogram>`
    - :class:`HistogramSeries <highcharts_maps.options.series.histogram.HistogramSeries>`
  * - :mod:`.options.series.item <highcharts_maps.options.series.item>`
    - :class:`ItemSeries <highcharts_maps.options.series.item.ItemSeries>`
  * - :mod:`.options.series.labels <highcharts_maps.options.series.labels>`
    - :class:`SeriesLabel <highcharts_maps.options.series.labels.SeriesLabel>`
      :class:`Box <highcharts_maps.options.series.labels.Box>`
  * - :mod:`.options.series.networkgraph <highcharts_maps.options.series.networkgraph>`
    - :class:`NetworkGraphSeries <highcharts_maps.options.series.networkgraph.NetworkGraphSeries>`
  * - :mod:`.options.series.organization <highcharts_maps.options.series.organization>`
    - :class:`OrganizationSeries <highcharts_maps.options.series.organization.OrganizationSeries>`
  * - :mod:`.options.series.packedbubble <highcharts_maps.options.series.packedbubble>`
    - :class:`PackedBubbleSeries <highcharts_maps.options.series.packedbubble.PackedBubbleSeries>`
  * - :mod:`.options.series.pareto <highcharts_maps.options.series.pareto>`
    - :class:`ParetoSeries <highcharts_maps.options.series.pareto.ParetoSeries>`
  * - :mod:`.options.series.pictorial <highcharts_maps.options.series.pictorial>`
    - :class:`PictorialSeries <highcharts_maps.options.series.pictorial.PictorialSeries>`
      :class:`PictorialPaths <highcharts_maps.options.series.pictorial.PictorialPaths>`
  * - :mod:`.options.series.pie <highcharts_maps.options.series.pie>`
    - :class:`PieSeries <highcharts_maps.options.series.pie.PieSeries>`
      :class:`VariablePieSeries <highcharts_maps.options.series.pie.VariablePieSeries>`
  * - :mod:`.options.series.polygon <highcharts_maps.options.series.polygon>`
    - :class:`PolygonSeries <highcharts_maps.options.series.polygon.PolygonSeries>`
  * - :mod:`.options.series.pyramid <highcharts_maps.options.series.pyramid>`
    - :class:`PyramidSeries <highcharts_maps.options.series.pyramid.PyramidSeries>`
      :class:`Pyramid3DSeries <highcharts_maps.options.series.pyramid.Pyramid3DSeries>`
  * - :mod:`.options.series.sankey <highcharts_maps.options.series.sankey>`
    - :class:`SankeySeries <highcharts_maps.options.series.sankey.SankeySeries>`
  * - :mod:`.options.series.scatter <highcharts_maps.options.series.scatter>`
    - :class:`ScatterSeries <highcharts_maps.options.series.scatter.ScatterSeries>`
      :class:`Scatter3DSeries <highcharts_maps.options.series.scatter.Scatter3DSeries>`
  * - :mod:`.options.series.series_generator <highcharts_maps.options.series.series_generator>`
    - :func:`create_series_obj() <highcharts_maps.options.series.series_generator.create_series_obj>`
  * - :mod:`.options.series.spline <highcharts_maps.options.series.spline>`
    - :class:`SplineSeries <highcharts_maps.options.series.spline.SplineSeries>`
  * - :mod:`.options.series.sunburst <highcharts_maps.options.series.sunburst>`
    - :class:`SunburstSeries <highcharts_maps.options.series.sunburst.SunburstSeries>`
  * - :mod:`.options.series.tiledwebmap <highcharts_maps.options.series.tiledwebmap'>`
    - :class:`TiledWebMapSeries <highcharts_maps.options.series.tiledwebmap.TiledWebMapSeries>`
  * - :mod:`.options.series.timeline <highcharts_maps.options.series.timeline>`
    - :class:`TimelineSeries <highcharts_maps.options.series.timeline.TimelineSeries>`
  * - :mod:`.options.series.treegraph <highcharts_maps.options.series.treegraph>`
    - :class:`TreegraphSeries <highcharts_maps.options.series.treegraph.TreegraphSeries>`
  * - :mod:`.options.series.treemap <highcharts_maps.options.series.treemap>`
    - :class:`TreemapSeries <highcharts_maps.options.series.treemap.TreemapSeries>`
  * - :mod:`.options.series.vector <highcharts_maps.options.series.vector>`
    - :class:`VectorSeries <highcharts_maps.options.series.vector.VectorSeries>`
  * - :mod:`.options.series.venn <highcharts_maps.options.series.venn>`
    - :class:`VennSeries <highcharts_maps.options.series.venn.VennSeries>`
  * - :mod:`.options.series.wordcloud <highcharts_maps.options.series.wordcloud>`
    - :class:`WordcloudSeries <highcharts_maps.options.series.wordcloud.WordcloudSeries>`
  * - :mod:`.options.sonification <highcharts_maps.options.sonification>`
    - :class:`SonificationOptions <highcharts_maps.options.sonification.SonificationOptions>`
  * - :mod:`.options.sonification.grouping <highcharts_maps.options.sonification.grouping>`
    - :class:`PointGrouping <highcharts_maps.options.sonification.grouping.SonificationGrouping>`
  * - :mod:`.options.sonification.mapping <highcharts_maps.options.sonification.mapping>`
    - :class:`SonificationMapping <highcharts_maps.options.sonification.mapping.SonificationMapping>`
      :class:`AudioParameter <highcahrts_core.options.sonification.mapping.AudioParameter>`
      :class:`AudioFilter <highcharts_maps.options.sonification.mapping.AudioFilter>`
      :class:`PitchParameter <highcharts_maps.options.sonification.mapping.PitchParameter>`
      :class:`TremoloEffect <highcahrts_core.options.sonification.mapping.TremoloEffect>`
  * - :mod:`.options.sonification.track_configurations <highcharts_maps.options.sonification.track_configurations>`
    - :class:`InstrumentTrackConfiguration <highcharts_maps.options.sonification.track_configurations.InstrumentTrackConfiguration>`
      :class:`SpeechTrackConfiguration <highcharts_maps.options.sonification.track_configurations.SpeechTrackConfiguration>`
      :class:`ContextTrackConfiguration <highcharts_maps.options.sonification.track_configurations.ContextTrackConfiguration>`
      :class:`TrackConfigurationBase <highcharts_maps.options.sonification.track_configurations.TrackConfigurationBase>`
      :class:`ActiveWhen <highcharts_maps.options.sonification.track_configurations.ActiveWhen>`
  * - :mod:`.options.subtitle <highcharts_maps.options.subtitle>`
    - :class:`Subtitle <highcharts_maps.options.subtitle.Subtitle>`
  * - :mod:`.options.time <highcharts_maps.options.time>`
    - :class:`Time <highcharts_maps.options.time.Time>`
  * - :mod:`.options.title <highcharts_maps.options.title>`
    - :class:`Title <highcharts_maps.options.title.Title>`
  * - :mod:`.options.tooltips <highcharts_maps.options.tooltips>`
    - :class:`Tooltip <highcharts_maps.options.tooltips.Tooltip>`
