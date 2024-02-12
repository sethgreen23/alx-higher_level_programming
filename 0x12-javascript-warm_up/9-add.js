#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    a = parseInt(a);
    b = parseInt(b);
    console.log(`${a + b}`);
  }
}

const args = process.argv;
const a = args[2];
const b = args[3];
add(a, b);
