#!/usr/bin/node
// squar
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let m = 0; m < size; m++) {
    let row = '';
    for (let e = 0; e < size; e++) row += 'X';
    console.log(row);
  }
}
