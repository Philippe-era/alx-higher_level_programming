#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let initial = 0; initial < list.length; initial++) {
    if (searchElement === list[initial]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};

