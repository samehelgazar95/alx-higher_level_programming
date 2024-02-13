#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  args.slice(3).sort();
  console.log(args[2]);
}
