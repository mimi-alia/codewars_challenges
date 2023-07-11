// Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

// Examples:

// spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
// spinWords( "This is a test") => returns "This is a test" 
// spinWords( "This is another test" )=> returns "This is rehtona test"

function spinWords(string){
    //split string into a list to iterate over
    const stringList = string.split(' ');
    //initiate empty list to store new words
    let spinnedWords = [];
    
    // for the every word in the list of words
    for (let i=0; i< stringList.length; i++){
      // if the word is shorter than 5 characters, add it directly to the list
      if (stringList[i].length < 5){
        spinnedWords.push(stringList[i]);
      // if the word is longer than or equal to 5 characters
        // split each character into a list of characters, reverse the order
        // and join it back into a string, then add it to the list
      } else {
        spinnedWords.push(stringList[i].split('').reverse().join(''));
      }
    }
    return spinnedWords.join(' ');
  }