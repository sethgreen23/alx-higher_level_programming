#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const fileA = args[2];
const fileB = args[3];
const fileC = args[4];
// Read from fileA
fs.readFile(fileA, (err, dataA) => {
  if (err) throw err;

  // Read from fileB
  fs.readFile(fileB, (err, dataB) => {
    if (err) throw err;

    // Concatenate contents of fileA and fileB
    const concatenatedData = dataA.toString() + dataB.toString();

    // Write to fileC
    fs.writeFile(fileC, concatenatedData, (err) => {
      if (err) throw err;
    });
  });
});
