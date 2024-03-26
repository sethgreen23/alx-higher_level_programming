#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const fName = args[2];
const content = args[3];
if (fName) {
  fs.writeFile(fName, content, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
