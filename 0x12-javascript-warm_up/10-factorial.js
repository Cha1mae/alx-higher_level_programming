#!/usr/bin/node
// prints a fact
function factorial (j) {
  return j === 0 || isNaN(j) ? 1 : j * factorial(j - 1);
}

console.log(factorial(Number(process.argv[2])));
