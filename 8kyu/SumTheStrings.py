# Create a function that takes 2 nonnegative integers in form of a string as an input, and outputs the sum (also as a string):

# Example: (Input1, Input2 -->Output)

# "4",  "5" --> "9"
# "34", "5" --> "39"

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))   