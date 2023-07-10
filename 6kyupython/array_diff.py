# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]


# Check that each item in a does not equal any item in break
def array_diff(a, b):

# Create lists of unqiue values from both lists
    set_a, set_b = set(a), set(b)

# Filter values from unique b list from the unique a list 
    filtered_list = [*set_a.difference(set_b)]

# Filter original a list with values from unique a list so that only unique values in a are selected 
    return [ x for x in a for y in filtered_list if x == y]