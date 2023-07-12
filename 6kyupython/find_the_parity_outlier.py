# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# Examples

# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
# To find an outlier, numbers need to be converted to booleans to target the single
# outlier
    
#   Convert list of numbers to a boolean list where even numbers
#   are true and odd numbers are false
    bool_list = [x%2==0 for x in integers]
    
#   For every item in the boolean list, if the count of a value in the list is 
#   1, then it is the unique value, and you can use its index to subset
#   the original number list for the outlier
    
    for k,i in enumerate(bool_list):
        if bool_list.count(i) ==1:
            return integers[k]