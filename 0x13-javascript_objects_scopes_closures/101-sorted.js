#!/usr/bin/node
const dict = require('./101-data').dict;

const first_list = Object.entries(dict);
const new_values = Object.values(dict);
const new_values = [...new Set(new_values)];
const new_dictionary = {};
for (const join in new_values) {
  const new_list = [];
  for (const k in first_list) {
    if (first_list[k][1] === new_values[join]) {
      new_list.unshift(first_list[k][0]);
    }
  }
  new_dictionary[new_values[join]] = new_list;
}
console.log(new_dictionary);

