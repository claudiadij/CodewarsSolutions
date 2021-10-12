# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Example:

# Kata.MakeNegative(1); // return -1
# Kata.MakeNegative(-5); // return -5
# Kata.MakeNegative(0); // return 0

def make_negative(number):
    if number > 0: 
        return number*(-1)
    else:
        return number