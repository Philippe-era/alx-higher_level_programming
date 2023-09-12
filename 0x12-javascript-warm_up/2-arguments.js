#!/usr/bin/node
const count_letters = process.argv.length;
console.log(count_letters === 2 ? 'No argument' : count_letters === 3 ? 'Argument found' : 'Arguments found');

