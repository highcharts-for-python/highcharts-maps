{
  data: [
      {
       color: '#ccc',
       from: 'some-id-goes-here',
       to: 'some-id-goes-here',
       weight: 1,

       accessibility: {
           description: 'Some description goes here',
           enabled: true
       },
       className: 'some-class-name',
       color: '#ccc',
       colorIndex: 2,
       custom: {
           'some_key': 123,
           'other_key': 456
       },
       description: 'Some description goes here',
       events: {
           click: function(event) { return true; },
           drag: function(event) { return true; },
           drop: function(event) { return true; },
           mouseOut: function(event) { return true; }
       },
       id: 'some-id-goes-here',
       labelrank: 3,
       name: 'Some Name Goes here',
       selected: false
      },
      {
       color: '#ccc',
       from: 'some-id-goes-here',
       to: 'some-id-goes-here',
       weight: 1,

       accessibility: {
           description: 'Some description goes here',
           enabled: true
       },
       className: 'some-class-name',
       color: '#ccc',
       colorIndex: 2,
       custom: {
           'some_key': 123,
           'other_key': 456
       },
       description: 'Some description goes here',
       events: {
           click: function(event) { return true; },
           drag: function(event) { return true; },
           drop: function(event) { return true; },
           mouseOut: function(event) { return true; }
       },
       id: 'some-id-goes-here',
       labelrank: 3,
       name: 'Some Name Goes here',
       selected: false
      }
  ],
  linkWeight: 'invalid value',
  nodes: [
      {
        color: '#cccccc',
        colorIndex: 123,
        dataLabels: {
            align: 'center',
            allowOverlap: false,
            backgroundColor: '#cccccc',
            enabled: true,
            overflow: 'justify',
            shadow: false
        },
        id: 'some-id-goes-here',
        name: 'My Node Name',
        offsetHorizontal: 10,
        offsetVertical: '5%'
      },
      {
        color: '#cccccc',
        colorIndex: 123,
        dataLabels: {
            align: 'center',
            allowOverlap: false,
            backgroundColor: '#cccccc',
            enabled: true,
            overflow: 'justify',
            shadow: false
        },
        id: 'some-id-goes-here',
        name: 'My Node Name',
        offsetHorizontal: 10,
        offsetVertical: '5%'
      }
  ],
  offset: 'invalid value',

  id: 'some-id-goes-here',
  index: 3,
  legendIndex: 3,
  name: 'Series Name Goes Here',
  stack: 'stack-id',
  xAxis: 'some-id',
  yAxis: 0,
  zIndex: 3,

  borderColor: '#fff',
  borderWidth: 2,
  centeredLinks: true,
  colorByPoint: false,
  colorIndex: 2,
  colors: [
      '#fff',
      'ccc',
      {
        linearGradient: {
            x1: 0.123,
            x2: 0.567,
            y1: 0.891,
            y2: 0.987
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
      },
      {
        animation: {
            defer: 5
        },
        patternOptions: {
            aspectRatio: 0.5,
            backgroundColor: '#999999',
            id: 'some_id_goes_here',
            opacity: 0.5,
            width: 120,
            x: 5,
            y: 10
        },
        patternIndex: 2
      }
  ],
  equalNodes: true,
  levels: [
      {
       colorByPoint: false,
       dataLabels: {
         align: 'center',
         allowOverlap: true,
         animation: {
             defer: 5
         },
         backgroundColor: {
             linearGradient: {
                 x1: 0.123,
                 x2: 0.234,
                 y1: 0.345,
                 y2: 0.456
             },
             stops: [
                 [0.12, '#999'],
                 [0.34, '#fff']
             ]
         },
         borderColor: '#999999',
         borderRadius: 24,
         borderWidth: 1,
         className: 'some-class-name',
         color: '#000000',
         crop: true,
         defer: false,
         enabled: true,
         filter: {
             operator: '>=',
             property: 'some_property',
             value: 123
         },
         format: 'some format',
         formatter: function() { return true; },
         inside: true,
         nullFormat: 'some format',
         nullFormatter: function() { return true; },
         overflow: 'none',
         padding: 12,
         position: 'center',
         rotation: 0,
         shadow: false,
         shape: 'rect',
         style: 'style goes here',
         useHTML: false,
         verticalAlign: 'top',
         x: 10,
         y: 20,
         z: 0
       },
       linkOpacity: 0.5,
       states: {
         hover: {
             animation: {
                 duration: 123
             },
             borderColor: '#cccccc',
             brightness: 0.3,
             enabled: true
         },
         inactive: {
             enabled: true,
             opacity: 0.5
         },
         normal: {
             animation: {
                 defer: 24
             }
         },
         select: {
             color: '#ff0000',
             enabled: true
         }
       },
       borderColor: '#ccc',
       borderWidth: 1,
       level: 1
      },
      {
       colorByPoint: false,
       dataLabels: {
         align: 'center',
         allowOverlap: true,
         animation: {
             defer: 5
         },
         backgroundColor: {
             linearGradient: {
                 x1: 0.123,
                 x2: 0.234,
                 y1: 0.345,
                 y2: 0.456
             },
             stops: [
                 [0.12, '#999'],
                 [0.34, '#fff']
             ]
         },
         borderColor: '#999999',
         borderRadius: 24,
         borderWidth: 1,
         className: 'some-class-name',
         color: '#000000',
         crop: true,
         defer: false,
         enabled: true,
         filter: {
             operator: '>=',
             property: 'some_property',
             value: 123
         },
         format: 'some format',
         formatter: function() { return true; },
         inside: true,
         nullFormat: 'some format',
         nullFormatter: function() { return true; },
         overflow: 'none',
         padding: 12,
         position: 'center',
         rotation: 0,
         shadow: false,
         shape: 'rect',
         style: 'style goes here',
         useHTML: false,
         verticalAlign: 'top',
         x: 10,
         y: 20,
         z: 0
       },
       linkOpacity: 0.5,
       states: {
         hover: {
             animation: {
                 duration: 123
             },
             borderColor: '#cccccc',
             brightness: 0.3,
             enabled: true
         },
         inactive: {
             enabled: true,
             opacity: 0.5
         },
         normal: {
             animation: {
                 defer: 24
             }
         },
         select: {
             color: '#ff0000',
             enabled: true
         }
       },
       borderColor: '#ccc',
       borderWidth: 1,
       level: 1
      },
      {
       colorByPoint: false,
       dataLabels: {
         align: 'center',
         allowOverlap: true,
         animation: {
             defer: 5
         },
         backgroundColor: {
             linearGradient: {
                 x1: 0.123,
                 x2: 0.234,
                 y1: 0.345,
                 y2: 0.456
             },
             stops: [
                 [0.12, '#999'],
                 [0.34, '#fff']
             ]
         },
         borderColor: '#999999',
         borderRadius: 24,
         borderWidth: 1,
         className: 'some-class-name',
         color: '#000000',
         crop: true,
         defer: false,
         enabled: true,
         filter: {
             operator: '>=',
             property: 'some_property',
             value: 123
         },
         format: 'some format',
         formatter: function() { return true; },
         inside: true,
         nullFormat: 'some format',
         nullFormatter: function() { return true; },
         overflow: 'none',
         padding: 12,
         position: 'center',
         rotation: 0,
         shadow: false,
         shape: 'rect',
         style: 'style goes here',
         useHTML: false,
         verticalAlign: 'top',
         x: 10,
         y: 20,
         z: 0
       },
       linkOpacity: 0.5,
       states: {
         hover: {
             animation: {
                 duration: 123
             },
             borderColor: '#cccccc',
             brightness: 0.3,
             enabled: true
         },
         inactive: {
             enabled: true,
             opacity: 0.5
         },
         normal: {
             animation: {
                 defer: 24
             }
         },
         select: {
             color: '#ff0000',
             enabled: true
         }
       },
       borderColor: '#ccc',
       borderWidth: 1,
       level: 1
      }
  ],
  linkOpacity: 0.7,
  minLinkWidth: 1,
  nodeWidth: 6,
  reversed: false,

  accessibility: {
      description: 'Description goes here',
      enabled: true,
      exposeAsGroupOnly: true,
      keyboardNavigation: {
          enabled: true
      },
      point: {
          dateFormat: 'format string',
          dateFormatter: function() { return true; },
          describeNull: false,
          descriptionFormatter: function() { return true; },
          valueDecimals: 2,
          valueDescriptionFormat: 'format string',
          valuePrefix: '$',
          valueSuffix: 'USD'
      },
  },
  allowPointSelect: true,
  animation: {
      defer: 5
  },
  className: 'some-class-name',
  clip: false,
  color: '#fff',
  cursor: 'alias',
  custom: {
      'item1': 'some value',
      'item2': 'some value'
  },
  dashStyle: 'Dash',
  dataLabels: {
    align: 'center',
    allowOverlap: true,
    animation: {
        defer: 5
    },
    backgroundColor: {
        linearGradient: {
            x1: 0.123,
            x2: 0.234,
            y1: 0.345,
            y2: 0.456
        },
        stops: [
            [0.12, '#999'],
            [0.34, '#fff']
        ]
    },
    borderColor: '#999999',
    borderRadius: 24,
    borderWidth: 1,
    className: 'some-class-name',
    color: '#000000',
    crop: true,
    defer: false,
    enabled: true,
    filter: {
        operator: '>=',
        property: 'some_property',
        value: 123
    },
    format: 'some format',
    formatter: function() { return true; },
    inside: true,
    nullFormat: 'some format',
    nullFormatter: function() { return true; },
    overflow: 'none',
    padding: 12,
    position: 'center',
    rotation: 0,
    shadow: false,
    shape: 'rect',
    style: 'style goes here',
    useHTML: false,
    verticalAlign: 'top',
    x: 10,
    y: 20,
    z: 0
  },
  description: 'Description goes here',
  enableMouseTracking: true,
  events: {
    afterAnimate: function(event) { return true; },
    click: function(event) { return true; },
    hide: function(event) { return true; },
    mouseOut: function(event) { return true; },
    show: function(event) { return true; }
  },
  includeInDataExport: true,
  keys: [
      'somevalue',
      'somevalue',
      'somevalue'
  ],
  label: {
      boxesToAvoid: [
          {
           bottom: 12,
           left: -46,
           right: 84,
           top: 24
          },
          {
           bottom: 48,
           left: -46,
           right: 84,
           top: 86
          }
      ],
      connectorAllowed: true,
      connectorNeighbourDistance: 12,
      enabled: true,
      format: 'format string',
      formatter: function() { return true; },
      maxFontSize: 18,
      minFontSize: 6,
      onArea: false,
      style: 'some style string'
  },
  linkedTo: 'some_id',
  marker: {
    enabled: true,
    fillColor: '#cccccc',
    height: 24,
    lineWidth: 2,
    radius: 2,
    states: {
        hover: {
            enabled: true
        }
    },
    symbol: 'circle',
    width: 48
  },
  onPoint: {
      connectorOptions: {
          dashstyle: 'Dash',
          stroke: '#ccc',
          width: 2
      },
      id: 'some-id',
      position: {
          align: 'left',
          verticalAlign: 'top',
          x: 15,
          y: -46
      }
  },
  opacity: 0.2,
  point: {
      events: {
        click: function(event) { return true; },
        drag: function(event) { return true; },
        drop: function(event) { return true; },
        mouseOut: function(event) { return true; }
      }
  },
  pointDescriptionFormatter: function (point) { return true; },
  selected: false,
  showCheckbox: true,
  showInLegend: true,
  skipKeyboardNavigation: false,
  states: {
    hover: {
        animation: {
            duration: 123
        },
        borderColor: '#cccccc',
        brightness: 0.3,
        enabled: true
    },
    inactive: {
        enabled: true,
        opacity: 0.5
    },
    normal: {
        animation: {
            defer: 24
        }
    },
    select: {
        color: '#ff0000',
        enabled: true
    }
  },
  stickyTracking: true,
  threshold: 123,
  tooltip: {
    animation: true,
    backgroundColor: '#ccc',
    borderColor: '#999',
    borderRadius: 4,
    borderWidth: 1,
    className: 'some-class-name',
    clusterFormat: 'format string',
    dateTimeLabelFormats: {
      day: 'test',
      hour: 'test',
      millisecond: 'test',
      minute: 'test',
      month: 'test',
      second: 'test',
      week: 'test',
      year: 'test'
    },
    distance: 12,
    enabled: true,
    followPointer: true,
    followTouchMove: true,
    footerFormat: 'format string',
    formatter: function() { return true; },
    headerFormat: 'format string',
    headerShape: 'circle',
    hideDelay: 3,
    nullFormat: 'format string',
    nullFormatter: function() { return true; },
    outside: false,
    padding: 6,
    pointFormat: 'format string',
    pointFormatter: function() { return true; },
    positioner: function() { return true; },
    shadow: false,
    shape: 'rect',
    shared: false,
    snap: 4,
    split: false,
    stickOnContact: true,
    style: 'style string goes here',
    useHTML: false,
    valueDecimals: 2,
    valuePrefix: '$',
    valueSuffix: ' USD',
    xDateFormat: 'format string'
   },
  turboThreshold: 456,
  visible: true
}
