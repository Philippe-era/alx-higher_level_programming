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
      let square_draw = '';
      for (let join_square = 0; join_square < this.width; join_square++) {
        square_draw += 'X';
      }
      console.log(square_draw);
    }
  }

  rotate () {
    const rotate_square = this.width;
    this.width = this.height;
    this.height = rotate_square;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

