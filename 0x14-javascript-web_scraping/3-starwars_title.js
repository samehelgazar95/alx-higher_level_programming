#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}/`;

request.get(url, (err, res, body) => {
  err && console.log(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
