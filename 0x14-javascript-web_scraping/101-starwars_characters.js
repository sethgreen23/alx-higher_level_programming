#!/usr/bin/node

const request = require('request');
const args = process.argv;

const id = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
async function printCharacters (url) {
  try {
    const movieReq = await new Promise(function (resolve, reject) {
      return request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });
    const characters = JSON.parse(movieReq).characters;
    for (const character of characters) {
      const characterReq = await new Promise(function (resolve, reject) {
        return request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(body);
          }
        });
      });
      const name = JSON.parse(characterReq).name;
      console.log(name);
    }
  } catch (error) {
    console.log(error);
  }
}
printCharacters(url);
