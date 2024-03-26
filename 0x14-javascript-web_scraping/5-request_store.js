#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv;

const url = args[2];
const fName = args[3];
request(url, (error, response, body) => {
  if (!error) {
    const res = body;
    if (fName) {
      fs.writeFile(fName, res, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  }
});
