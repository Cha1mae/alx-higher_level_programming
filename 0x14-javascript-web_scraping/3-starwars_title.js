#!/usr/bin/node
// This script prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
