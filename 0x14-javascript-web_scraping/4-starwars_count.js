#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = args[2];
request(url, (error, response, body) => {
  if (!error) {
    const res = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < res.length; i++) {
      const characters = res[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
