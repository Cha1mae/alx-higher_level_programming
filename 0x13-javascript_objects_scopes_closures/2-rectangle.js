#!/usr/bin/node
// def a rec with w and l if 0 creates an empty object
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
};
