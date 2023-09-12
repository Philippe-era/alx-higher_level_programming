#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let initial = 0; initial < x; initial++) {
    console.log('C is fun');
  }
}

