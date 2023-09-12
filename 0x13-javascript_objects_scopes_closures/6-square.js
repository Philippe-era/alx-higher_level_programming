#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let initial = 0; initial < this.height; initial++) {
      let square_draw = '';
      for (let join_square = 0; join_square < this.width; join_square++) {
        square_draw += c;
      }
      console.log(square_draw);
    }
  }
}

module.exports = Square;

