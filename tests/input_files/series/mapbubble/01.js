{
  data: [
    {
      z: 123,
      dataLabels:  {
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
      drilldown: 'some-id-goes-here',
      geometry: {
        "geometry": {
          "coordinates": [-3.68, 40.4],
          "type": "Point"
        },
        "properties": {},
        "type": "Feature"
      }
    }
  ],

  borderColor: '#777',
  borderWidth: 2,
  dataAsColumns: false,
  lineColor: '#ccc',

  allAreas: true,
  joinBy: 'hc-key',

  displayNegative: false,
  jitter: {
    x: 123,
    y: 456
  },
  maxSize: 24,
  minSize: 6,
  sizeBy: 'width',
  sizeByAbsoluteValue: true,
  zMax: 6,
  zMin: 3,
  zThreshold: 50
}
