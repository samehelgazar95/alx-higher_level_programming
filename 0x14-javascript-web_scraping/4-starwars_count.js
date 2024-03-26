#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let counter = 0;

request.get(url, (err, res, body) => {
  err && console.log(err);

  const results = JSON.parse(body).results;

  results.forEach((e) => {
    e.characters.forEach((ele) => {
      if (ele.split('/')[5] === '18') counter++;
    });
  });

  console.log(counter);
});
