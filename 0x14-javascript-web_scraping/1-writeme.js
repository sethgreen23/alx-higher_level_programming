#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const fName = args[2];
const content = args[3];
if (fName) {
  fs.writeFile(fName, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
  });
}
