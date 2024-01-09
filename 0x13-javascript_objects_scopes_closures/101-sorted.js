#!/usr/bin/node

const { dict } = require('./101-data.js');
const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (newDict[value] === undefined) newDict[value] = [];
  newDict[value] = [...newDict[value], key];
}

console.log(newDict);
