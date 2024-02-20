#!/usr/bin/node
// This script reads a file, specified by the command line argument
// and prints its content to the console or an error message if
// an error occurs
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
