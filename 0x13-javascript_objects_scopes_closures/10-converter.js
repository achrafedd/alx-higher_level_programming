#!/usr/bin/node

exports.converter = function (base) {
  return function (num = 0) {
    return num.toString(base);
  };
};
