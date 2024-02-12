#!/usr/bin/node

const args = process.argv;
if (args.length < 3) {
  console.log('No argument');
} else if (args.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
