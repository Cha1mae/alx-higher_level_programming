#!/usr/bin/node
// This script prints all characters of a Star Wars movie in the same order as in the /films/ response
const rek = require('request');
const MI = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${MI}`;

function getCharacterName(url, callback) {
  rek(url, function (error, response, body) {
    if (error) {
      console.error('error:', error);
      return;
    }
    callback(JSON.parse(body).name);
  });
}

rek(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach((characterUrl) => {
    getCharacterName(characterUrl, function (name) {
      console.log(name);
    });
  });
});
