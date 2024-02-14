#!/usr/bin/node

const parentSquare = require('./5-square.js');

class Square extends parentSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
