#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) return;
    if (typeof w !== 'number' || typeof h !== 'number') return;
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
