# Given an array of numbers and an index, return the index of the least number larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

# Multiple correct answers may be possible. In this case, return any one of them.
# The given index will be inside the given array.
# The given array will, therefore, never be empty.

def least_larger(a, i): 
    dict = {}
    for x in range(len(a)):
        if a[x] > a[i]:
            dict[a[x]] = x
    if len(dict) == 0:
        return -1
    else:
        mini = min(dict) 
        return dict[mini]