#!/usr/bin/node

const args = process.argv;
if (!args[2] || isNaN(parseInt(args[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args[2])}`);
}
