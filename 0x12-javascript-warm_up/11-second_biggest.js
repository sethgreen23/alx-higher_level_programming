#!/usr/bin/node

function maxValue (arr) {
  let maxV = parseInt(arr[2]);
  for (let i = 3; i < arr.length; i++) {
    const current = parseInt(arr[i]);
    if (current > maxV) {
      maxV = current;
    }
  }
  return (maxV);
}

function secondValue (arr) {
  const maxV = maxValue(arr);
  let i = 2;
  while (parseInt(args[i]) === maxV) {
    i++;
  }
  let second = parseInt(arr[i]);
  i++;
  for (; i < arr.length; i++) {
    const current = parseInt(arr[i]);
    if (current === maxV) {
      continue;
    }
    if (current > second) {
      second = current;
    }
  }
  return (second);
}
const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  console.log(`${secondValue(args)}`);
}
