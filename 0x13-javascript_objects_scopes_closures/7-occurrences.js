#!/usr/bin/node
// number of accurances in a list
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((cnt, current) => current === searchElement ? cnt + 1 : cnt, 0);
};
