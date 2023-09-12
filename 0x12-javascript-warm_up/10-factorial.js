#!/usr/bin/node
function factorial (num_check) {
  return num_check === 0 || isNaN(num_check) ? 1 : num_check * factorial(num_check - 1);
}

console.log(factorial(Number(process.argv[2])));

