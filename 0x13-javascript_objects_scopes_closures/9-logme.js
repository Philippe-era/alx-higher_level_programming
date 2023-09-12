#!/usr/bin/node
let start = 0;

exports.logMe = function (item) {
  console.log(start + ': ' + item);
  start++;
};

