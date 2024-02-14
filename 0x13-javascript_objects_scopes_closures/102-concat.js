#!/usr/bin/node

function concatsFiles(src1, src2, dest) {
  // Sync
  const fs = require('node:fs');
  const fileA = fs.readFileSync(src1, 'utf8');
  const fileB = fs.readFileSync(src2, 'utf8');

  fs.appendFileSync(dest, fileA);
  fs.appendFileSync(dest, fileB);
}

concatsFiles('fileA', 'fileB', 'fileC');

// Async >> use Promise to handle
// fs.readFile('fileA', 'utf8', (err, data) => {
//   if (err) throw err;
//   fileA = data;
// });

// fs.readFile('fileB', 'utf8', (err, data) => {
//   if (err) throw err;
//   fileB = data;
// });
