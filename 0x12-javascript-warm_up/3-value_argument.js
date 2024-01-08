#!/usr/bin/node
// fst arg is printd
const arg = process.argv[2];

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
