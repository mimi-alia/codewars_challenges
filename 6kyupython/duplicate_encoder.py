# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
# Examples

# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

# Notes

# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!


def duplicate_encode(word):
#     get a count of each character in the word, if it is more than one, replace
#     it with ")", else "("
    
    words = list(word.lower())
    
    new_word = ""
    
    for i in words:
        if words.count(i) > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word