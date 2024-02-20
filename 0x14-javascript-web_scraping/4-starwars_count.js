#!/usr/bin/node
// This script prints the number of Star Wars movies where the character “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  let count = 0;
  const films = JSON.parse(body).results;
  films.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.endsWith('/18/')) {
        count += 1;
      }
    });
  });
  console.log(count);
});
