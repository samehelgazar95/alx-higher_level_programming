#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, res) => {
  err ? console.log(err) : console.log(res);
});
