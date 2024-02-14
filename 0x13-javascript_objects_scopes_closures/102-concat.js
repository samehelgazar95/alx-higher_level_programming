#!/usr/bin/node

const fs = require('node:fs');
const args = process.argv.slice(2).map((arg) => arg.toString());

// Sync
fs.appendFileSync(args[2], fs.readFileSync(args[0], 'utf8'));
fs.appendFileSync(args[2], fs.readFileSync(args[1], 'utf8'));

// Async >> use Promise to handle
// fs.readFile('fileA', 'utf8', (err, data) => {
//   if (err) throw err;
//   fileA = data;
// });

// fs.readFile('fileB', 'utf8', (err, data) => {
//   if (err) throw err;
//   fileB = data;
// });
