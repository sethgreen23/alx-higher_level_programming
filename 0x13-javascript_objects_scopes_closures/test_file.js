#!/usr/bin/node

const fs = require('fs').promises;
async function loadFile(filename1, filename2, filename3) {
    const data = await fs.readFile(filename1, "utf-8");
    const data2 = await fs.readFile(filename2, "utf-8");
    fullData = data+data2;
    fs.writeFile(filename3, fullData);
}
loadFile(process.argv[2], process.argv[3], process.argv[4]);
