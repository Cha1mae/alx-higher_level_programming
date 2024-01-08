#!/usr/bin/node
// dependin on ars passd write a script
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
