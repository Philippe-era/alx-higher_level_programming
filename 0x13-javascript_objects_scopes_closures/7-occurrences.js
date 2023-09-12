#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let none0currences 0;
  for (let initial = 0; initial < list.length; initial++) {
    if (searchElement === list[initial]) {
      none0currences++;
    }
  }
  return none0currences;
};

