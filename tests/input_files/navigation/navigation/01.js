{
  bindingsClassName: 'some-class-name',
  buttonOptions: {
    enabled: true,
    text: 'Button Label',
    theme: {
        'fill': '#fff',
        'stroke': '#ccc'
    },
    y: 0
  },
  events: {
    closePopup: function (event) { return true; },
    selectButton: function (event) {return true;},
    showPopup: function(event) {return true;}
  },
  iconsURL: 'https://www.somewhere.com/'
}
