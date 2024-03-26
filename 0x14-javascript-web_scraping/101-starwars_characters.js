#!/usr/bin/node

const request = require('request');
const args = process.argv;

const id = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Function to fetch character name from URL
const getCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (err, resp, bod) => {
      if (err) {
        reject(err);
      } else {
        const name = JSON.parse(bod).name;
        resolve(name);
      }
    });
  });
};

// Main function to fetch movie characters and print their names
const printMovieCharacters = async () => {
  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });

    const characters = JSON.parse(movieResponse).characters;
    for (const character of characters) {
      const characterName = await getCharacterName(character);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

// Call the main function
printMovieCharacters();
