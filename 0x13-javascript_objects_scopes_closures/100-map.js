#!/usr/bin/node

const oldArr = require('./100-data.js').list;
const newArr = oldArr.map((num, idx) => num * idx);

console.log(oldArr);
console.log(newArr);
