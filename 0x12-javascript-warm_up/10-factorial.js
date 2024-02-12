#!/usr/bin/node

function factorial (n) {
  if (n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const args = process.argv;
const num = parseInt(args[2]);
if (!args[2] || isNaN(num)) {
  console.log('1');
} else {
  console.log(`${factorial(num)}`);
}
