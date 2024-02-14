#!/usr/bin/node

const fs = require('node:fs');
const args = process.argv;

// Sync
const fileA = fs.readFileSync(args[2], 'utf8');
const fileB = fs.readFileSync(args[3], 'utf8');

fs.appendFileSync(args[4], fileA);
fs.appendFileSync(args[4], fileB);

// Async >> use Promise to handle
// fs.readFile('fileA', 'utf8', (err, data) => {
//   if (err) throw err;
//   fileA = data;
// });

// fs.readFile('fileB', 'utf8', (err, data) => {
//   if (err) throw err;
//   fileB = data;
// });
