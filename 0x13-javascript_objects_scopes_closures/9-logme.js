#!/usr/bin/node
// alrdy printed args are printed with new value
let count = 0;
exports.logMe = function (item) { console.log(`${count++}: ${item}`); };
