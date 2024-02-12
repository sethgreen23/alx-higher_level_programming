#!/usr/bin/node

const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  const copyArr = [];
  for (let i = 2, j = 0; i < args.length; i++) {
    copyArr[j++] = parseInt(args[i]);
  }
  const maxValue = Math.max(...copyArr);
  const finalArr = [];
  for (let i = 0, j = 0; i < copyArr.length; i++) {
    if (copyArr[i] === maxValue) {
      continue;
    }
    finalArr[j++] = copyArr[i];
  }
  console.log(`${Math.max(...finalArr)}`);
}
