#!/usr/bin/node

const oldDict = require('./101-data.js').dict;
const newDict = {};

for (const [key, val] of Object.entries(oldDict)) {
  newDict[val] ? newDict[val].push(key) : (newDict[val] = [key]);
}

console.log(newDict);
