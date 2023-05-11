// In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
// Examples

// high_and_low("1 2 3 4 5")  # return "5 1"
// high_and_low("1 2 -3 4 5") # return "5 -3"
// high_and_low("1 9 3 4 -5") # return "9 -5"

/*function highAndLow(numbers){
  //set max and min to first item in numbers list
  let maxNum = numbers[0]
  let minNum = numbers[0]
  //convert numbers string to an array using split (turns it into array)
  //and map to iterate over each item and convert them from str to num
  let numArr = numbers.split(' ').map(x => Number(x))
  //for each item, add to max if more than last, add to min if less than min                               
  for (i=0; i<numArr.length; i++){
    if (numArr[i] > maxNum){
      maxNum = numArr[i]
    } else if (numArr[i] < minNum){
      minNum = numArr[i]
    }
  }
  let maxMin = `${maxNum} ${minNum}`
  return maxMin
}
*/

function highAndLow(numbers){
    var newArray = numbers.split(' ').map(Number)
    
  
    let highestNum = Math.max(...newArray);
    let lowestNum = Math.min(...newArray);
    return(`${highestNum} ${lowestNum}`)
  }
  /*
  function highAndLow(numbers){
    let arr = numbers.split(' ').map(Number);  
    return Math.max(...arr) + ' ' + Math.min(...arr);
  }*/