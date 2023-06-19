# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

def abbrev_name(name):
    nameArr = name.split(' ')
    abbrevName= [i[0] for i in nameArr]
    # return str(abbrevName[0]) + '.' + str(abbrevName[1])
    return '{}.{}'.format(str(abbrevName[0]).upper(), str(abbrevName[1]).upper())