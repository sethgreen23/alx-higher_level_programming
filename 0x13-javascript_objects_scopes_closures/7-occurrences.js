#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((num) => num === searchElement).length;
};
