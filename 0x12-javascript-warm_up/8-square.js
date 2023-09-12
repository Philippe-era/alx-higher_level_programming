#!/usr/bin/node
const square_print = Math.floor(Number(process.argv[2]));
if (isNaN(square_print)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < square_print; row++) {
    let row_draw = '';
    for (let column = 0; column < square_print; column++) row_draw += 'X';
    console.log(row_draw);
  }
}
