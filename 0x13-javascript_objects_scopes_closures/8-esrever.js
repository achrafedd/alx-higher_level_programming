#!/usr/bin/node

exports.esrever = function (list) {
  const length = list.length;
  let i;
  const reversdList = [];

  for (i = length - 1; i >= 0; i--) {
    reversdList.push(list[i]);
  }
  return reversdList;
};
