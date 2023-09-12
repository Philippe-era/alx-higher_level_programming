#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let initial = 0; initial < this.height; initial++) {
      let square = '';
      for (let join_square = 0; join_square < this.width; join_square++) {
        square += 'X';
      }
      console.log(square);
    }
  }
}

module.exports = Rectangle;

