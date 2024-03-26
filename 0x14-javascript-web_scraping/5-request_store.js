#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const findMe = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (err, res, body) => {
  let counter = 0;
  err && console.log(err);
  const data = JSON.parse(body);
  const results = data.results;

  results.forEach((e) => {
    e.characters.forEach((ele) => {
      if (ele === findMe) counter++;
    });
  });

  console.log(counter);
});
