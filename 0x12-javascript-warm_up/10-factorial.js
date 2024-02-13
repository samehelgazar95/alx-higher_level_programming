#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 1) {
    return 1;
  }

  return factorial(n - 1) * n;
}

const num = Number(process.argv[2]);
console.log(factorial(num));
