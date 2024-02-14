#!/usr/bin/node

const fs = require('node:fs');

// Sync
const fileA = fs.readFileSync('fileA', 'utf8');
const fileB = fs.readFileSync('fileB', 'utf8');

fs.appendFileSync('fileC', fileA);
fs.appendFileSync('fileC', fileB);

// Async >> use Promise to handle
// fs.readFile('fileA', 'utf8', (err, data) => {
//   if (err) throw err;
//   fileA = data;
// });

// fs.readFile('fileB', 'utf8', (err, data) => {
//   if (err) throw err;
//   fileB = data;
// });
