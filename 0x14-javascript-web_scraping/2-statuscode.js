#!/usr/bin/node
// This script displays the status code of a GET request to a URL specified by the command line argument
const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
