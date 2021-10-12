# Create a function with two arguments that will return an array of the first (n) multiples of (x).

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array (or list in Python, Haskell or Elixir).

def count_by(x, n):
    newlist = []
    for i in range(x, (x*n)+1):
        if i%x == 0:
            newlist.append(i)
    return newlist