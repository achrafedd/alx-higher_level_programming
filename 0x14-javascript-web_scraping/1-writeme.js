#!/usr/bin/node
const { writeFile } = require('fs/promises');
const file = process.argv[2];
const content = process.argv[3];

try {
  writeFile(`./${file}`, content, { encoding: 'utf8' });
} catch (e) {
  console.log(e);
}
