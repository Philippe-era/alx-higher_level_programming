#!/usr/bin/node
const number_to_up = Math.floor(Number(process.argv[2]));
console.log(isNaN(number_to_up) ? 'Not a number' : `My number: ${number_to_up}`);
