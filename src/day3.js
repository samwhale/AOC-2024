import { readFile } from '../utils/parse_data.js';

const data = readFile('../data/day3.txt');

const test = `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`;
const part1Regexp = /mul\(([0-9]+),([0-9]+)\)/g;

function parse(str) {
  let result = 0;
  const matches = str.matchAll(part1Regexp);

  for (const match of matches) {
    result += Number(match[1]) * Number(match[2]);
  }

  return result;
}

function parseWithDoAndDont(str) {
  const splitOnDo = str.split('do()');

  let result = 0;
  for (const doSplit of splitOnDo) {
    const splitOnDont = doSplit.split("don't()");

    result += parse(splitOnDont[0]);
  }

  return result;
}

console.log('Part 1', parse(data));
console.log('Part 2', parseWithDoAndDont(data));
