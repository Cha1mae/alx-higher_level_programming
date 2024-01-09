#!/usr/bin/node
// inheriting from square 5 creats instance c
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let maki = 0; maki < this.height; maki++) console.log(c.repeat(this.width));
    }
  }
};
