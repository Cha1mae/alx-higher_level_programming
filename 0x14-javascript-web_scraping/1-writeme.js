#!/usr/bin/node
// This script writes a string to a file, specified by the command line argument
// and prints its content to the console or an error message if
// an error occurs
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
