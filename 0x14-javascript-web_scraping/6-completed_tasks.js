#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = args[2];
request(url, (error, response, body) => {
  if (!error) {
    const res = JSON.parse(body);
    const completedDict = {};
    for (const user of res) {
      if (user.completed === true) {
        if (completedDict[`${user.userId}`] === undefined) { completedDict[`${user.userId}`] = 1; } else { completedDict[`${user.userId}`] += 1; }
      }
    }
    console.log(completedDict);
  }
});
