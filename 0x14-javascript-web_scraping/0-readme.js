#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const fName = args[2];
if (fName) {
  fs.readFile(fName, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
