#!/usr/bin/node
exports.esrever = function (list) {
  let le = list.length - 1;
  let i = 0;
  while ((le - i) > 0) {
    const tmp = list[le];
    list[le] = list[i];
    list[i] = tmp;
    i++;
    le--;
  }
  return list;
};
