################################################################
:mod:`.series <highcharts_maps.options.series>`
################################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  arcdiagram
  area
  bar
  base
  bellcurve
  boxplot
  bubble
  bullet
  data/index
  dependencywheel
  dumbbell
  flowmap
  funnel
  gauge
  heatmap
  histogram
  item
  labels
  map
  mapbubble
  mapline
  mappoint
  networkgraph
  organization
  packedbubble
  pareto
  pictorial
  pie
  points
  polygon
  pyramid
  sankey
  scatter
  series_generator
  spline
  sunburst
  tiledwebmap
  timeline
  treegraph
  treemap
  vector
  venn
  wordcloud

-------------------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
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
