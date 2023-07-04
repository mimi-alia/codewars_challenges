# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

#     years divisible by 4 are leap years
#     but years divisible by 100 are not leap years
#     but years divisible by 400 are leap years

# Additional Notes:

#     Only valid years (positive integers) will be tested, so you don't have to validate them

# Examples can be found in the test fixture.

def isLeapYear(year):
    # Description of code:
    # Year must be both divisible by 4 while also being indivisible by 100, and then divisible by 400
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

