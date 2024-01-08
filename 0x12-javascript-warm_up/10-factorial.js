#!/usr/bin/node
const number = parseInt(process.argv[2]);

function factorial (number) {
  if (number === 1 || isNaN(number)) {
    return 1;
  }
  return number * factorial(number - 1);
}

console.log(factorial(number));
