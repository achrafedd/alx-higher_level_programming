#!/usr/bin/node
const [,, ...numbers] = process.argv;
const length = numbers.length;
const output =
  length > 1
    ? numbers.map((number) => +number).sort((a, b) => a - b)[length - 2]
    : 0;
console.log(output);
