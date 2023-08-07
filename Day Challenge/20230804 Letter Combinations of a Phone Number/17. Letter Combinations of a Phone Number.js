var letterCombinations = function (digits) {
  if (digits === '') return [];
  map = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
  };

  let results = [];

  const dfs = (c, s) => {
    if (s.length === digits.length) {
      results.push(s.join(''));
      return;
    }

    for (let i = c; i < digits.length; i++) {
      for (let n of map[digits[i]]) {
        s.push(n);
        dfs(i + 1, s);
        s.pop();
      }
    }
  };

  dfs(0, []);

  return results;
};
