// Digital root is the recursive sum of all the digits in a number.

// Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
// Examples

//     16  -->  1 + 6 = 7
//    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
// 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
// 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


function digitalRoot(n) {
    //create a list of numbers by converting the number n to a string (make it iterable),
    //then splitting it at each digit to a list and converting each individual list item to a number again
    const numberList = n.toString().split('').map(x => Number(x));
    //sum will hold the sum of each digit
    let sum = 0;
    
    //for each digit in the list of numbers, add each to the sum
    for (i=0; i< numberList.length; i++){
      sum += numberList[i];
    }

    //if the sum is less than 10 (thus a single digit), the kata has been fulfilled
    if(sum < 10){
      return sum;
      
    //if the sum is more than one digit, feed it back to the function and it will continue until it is one digit  
    } else {
      return digitalRoot(sum); 
      }
  }