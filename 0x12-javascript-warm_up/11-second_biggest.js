#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const a = process.argv.slice(2).map(Number);
  const sec = a.sort(function (a, b) { return b - a; })[1];
  console.log(sec);
}
