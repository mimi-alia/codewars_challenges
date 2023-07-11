# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
# short version using list comprehension 
#     return ' '.join(x[::-1] if len(x) >= 5 else x for x in sentence.split())

# human-legible version using if-else statements and for loop
# Split the string into a list so that you can iterate over each individual word
# and append them in order to a list (spinned) if the length of the word is more than
# 5 characters

    # initialize list to store words
    spinned = []
    # for each word in the sentence list
    for word in sentence.split():
        #if the length of the word is less than 5 characers, add it directly to spinned
        if len(word) < 5:
            spinned.append(word)
        # if the word is more than or equal to 5 characters, reverse it and add it to the list
        else:
            spinned.append(word[::-1])
        # return the spinned list as a string
    return ' '.join(spinned)