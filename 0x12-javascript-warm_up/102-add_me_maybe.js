#!/usr/bin/node
// calls a function and inc a func
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
