#!/usr/bin/node
// This script prints all characters of a Star Wars movie where the episode number matches a given integer
const rek = require('request');
const MI = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${MI}`;

rek(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach((characterUrl) => {
    rek(characterUrl, function (error, response, body) {
      if (error) {
        console.error('error:', error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
