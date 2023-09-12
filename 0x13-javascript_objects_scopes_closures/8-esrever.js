#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length - 1;
  let start = 0;
  while ((size - start) > 0) {
    const reverse_draw = list[size];
    list[size] = list[start];
    list[start] = reverse_draw;
    start++;
    size--;
  }
  return list;
};

