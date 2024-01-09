#!/usr/bin/node
// reverse a list
exports.esrever = function (list) {
  return list.reduceRight(function (array, curnt) {
    array.push(curnt);
    return array;
  }, []);
};
