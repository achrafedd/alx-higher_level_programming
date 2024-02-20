#!/usr/bin/node
const { readFile } = require('fs/promises');
const file = process.argv[2];

const getContent = async () => {
  try {
    const contents = await readFile(file, { encoding: 'utf8' });
    console.log(contents);
  } catch (e) {
    console.log(e);
  }
};

getContent();
