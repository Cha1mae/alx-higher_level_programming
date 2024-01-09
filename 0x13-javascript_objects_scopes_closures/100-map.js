#!/usr/bin/node
// import array to a new array
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((m, x) => m * x));
