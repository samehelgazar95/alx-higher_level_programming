#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, res, body) => {
  err && console.log(err);
  fs.writeFile(filePath, body, 'utf8', (err) => {
    err && console.log(err);
  });
});
