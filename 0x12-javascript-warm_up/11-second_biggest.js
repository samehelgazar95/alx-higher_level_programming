#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const newArgs = args.slice(2).sort((a, b) => b - a);
  console.log(newArgs[1]);
}
