// Simple, given a string of words, return the length of the shortest word(s).

// String will never be empty and you do not need to account for different data types.

function findShort(s){
    let sArray = s.split(' ')
    let result = sArray[0]
    for (i=0; i<sArray.length; i++){
      if (sArray[i].length < result.length){
        result = sArray[i];
      }
    } return result.length;
  }