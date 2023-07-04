# Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
# Examples

#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


def digital_root(n):
    # Create a list of each digits within the given number "n"

    # create a stringified number with which you can iterate over, then unpack each digit converted to an int (num_list)

    str_list= [*str(n)]
    num_list = [*map(lambda i : int(i), str_list)]

    # create a variable, "results", to store the sum
    results = 0
    
    # add the sum of digits to the results variable
    for i in num_list:
        results+=i
        
    # While the length of the sum is more than 1 digit, continue adding the digits together until it is less than 1 digit

    while (len(str(results))) > 1:
        new_nums = [*map(lambda x : int(x), str(results))]
        # reset results to 0
        results = 0
        for y in new_nums:
            results+=y
        
    return results