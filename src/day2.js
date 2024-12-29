import { readFile } from '../utils/parse_data.js';

const data = readFile('../data/day2.txt')
  .split('\n')
  .map((row) => row.split(' ').map(Number));

function isSafeRow(row, allowMulligan = false) {
  if (row.length === 0) {
    throw new Error('Row is empty');
  }

  const increasing = row[0] < row[1];

  for (let i = 1; i < row.length; i++) {
    const difference = row[i] - row[i - 1];

    if ((increasing && difference < 0) || (!increasing && difference > 0)) {
      if (allowMulligan) {
        return row.some((_, index) => isSafeRow(row.slice(0, index).concat(row.slice(index + 1))));
      }

      return false;
    }

    const absoluteDifference = Math.abs(difference);

    if (absoluteDifference < 1 || absoluteDifference > 3) {
      if (allowMulligan) {
        return row.some((_, index) => isSafeRow(row.slice(0, index).concat(row.slice(index + 1))));
      }

      return false;
    }
  }

  return true;
}

console.log('Part 1', data.map((row) => isSafeRow(row)).filter(Boolean).length);
console.log('Part 2', data.map((row) => isSafeRow(row, true)).filter(Boolean).length);
