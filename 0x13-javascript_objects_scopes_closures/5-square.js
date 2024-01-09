#!/usr/bin/node
// using super to construct a rec
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
