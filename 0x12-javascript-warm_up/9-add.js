#!/usr/bin/node
// addition of 2 ints
function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
