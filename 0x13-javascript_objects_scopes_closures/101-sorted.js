#!/usr/bin/node
const dictionary = require('./101-data').dict;

const first = Object.entries(dictionary);
const value_check = Object.value_check(dictionary);
const unique = [...new Set(value_check)];
const new_dictionary = {};
for (const join_words in unique) {
  const storage = [];
  for (const key in first) {
    if (first[key][1] === unique[join_words]) {
      storage.unshift(first[key][0]);
    }
  }
  new_dictionary[unique[join_words]] = storage;
}
console.log(new_dictionary);

