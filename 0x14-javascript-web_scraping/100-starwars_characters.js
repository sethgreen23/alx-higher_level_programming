#!/usr/bin/node

const request = require('request');
const args = process.argv;

const id = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, resp, bod) => {
        if (!err) {
          const name = JSON.parse(bod).name;
          console.log(name);
        }
      });
    }
  }
});
