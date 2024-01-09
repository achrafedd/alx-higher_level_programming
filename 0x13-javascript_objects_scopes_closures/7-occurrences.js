#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i;
  let number = 0;
  const length = list.length;

  for (i = 0; i < length; i++) {
    if (list[i] === searchElement) number += 1;
  }
  return number;
};
