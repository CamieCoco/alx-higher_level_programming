#!/usr/bin/node
// script that imports an array and computes a new array
const list = require('./100-data').list;
console.log(list);
let i = 0;
const map1 = list.map(x => x * i++);
console.log(map1);
