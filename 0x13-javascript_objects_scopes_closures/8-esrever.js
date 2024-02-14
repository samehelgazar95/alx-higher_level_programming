#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  const len = list.length;

  for (let i = 0, j = len - 1; i < len; i++, j--) {
    reversed[i] = list[j];
  }

  return reversed;
};
