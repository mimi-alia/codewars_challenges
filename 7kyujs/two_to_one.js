// Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
// Examples:

// a = "xyaabbbccccdefww"
// b = "xxxxyyyyabklmopq"
// longest(a, b) -> "abcdefklmopqwxy"

// a = "abcdefghijklmnopqrstuvwxyz"
// longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"


function longest(s1, s2) {
    const string = s1+s2;
  //   let current = '';
    let results = [];
    
    for (i=0;i<string.length; i++){
      if (!results.includes(string[i])){
        results.push(string[i]);
      }
    }
    return results.sort().join('');
  }