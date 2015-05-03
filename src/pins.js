var piblaster = require("pi-blaster.js");

const RED = 11;
const GREEN = 13;
const BLUE = 15;

function Pins() {};

function transform(colorValue) {
  return (((value - 0) * (0 - 100)) / (255 - 0)) + 100;
};

Pins.prototype.apply = function(color) {
  piblaster.setPwm(RED, transform(color.red));
  piblaster.setPwm(GREEN, transform(color.green));
  piblaster.setPwm(BLUE, transform(color.blue));
};

module.exports = exports = new Pins();
