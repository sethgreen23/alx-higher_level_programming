#!/usr/bin/node

const args = process.argv;
if (!args[2] || isNaN(parseInt(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  let x = parseInt(args[2]);
  while (x > 0) {
    console.log('C is fun');
    --x;
  }
}
