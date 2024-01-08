#!/usr/bin/node
const cool = 'C is fun';
const number = parseInt(process.argv[2]);

if (!isNaN(number)) {
  let i = 0;
  while (i < number) {
    console.log(cool);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
