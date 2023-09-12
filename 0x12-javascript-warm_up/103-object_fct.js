#!/usr/bin/node
const myIncrement = {
  type: 'object',
  value: 12
};
console.log(myIncrement);

myIncrement.incr = function () {
  this.value++;
};

myIncrement.incr();
console.log(myIncrement);
myIncrement.incr();
console.log(myIncrement);
myIncrement.incr();

