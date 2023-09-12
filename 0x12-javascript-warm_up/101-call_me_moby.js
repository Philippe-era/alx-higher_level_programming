#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let initial = 0; initial < x; initial++) theFunction();
};

