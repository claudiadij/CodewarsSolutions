# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.

# Example

# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if len(arr) != 0 else []

# or

def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if len(arr) != 0 else []