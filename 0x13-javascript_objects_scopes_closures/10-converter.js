#!/usr/bin/node

exports.converter = function (base) {
  return function (num_convert) {
    return num_convert.toString(base);
  };
};

