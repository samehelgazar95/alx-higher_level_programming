#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, res) => {
  if (err) console.log(err);
});
