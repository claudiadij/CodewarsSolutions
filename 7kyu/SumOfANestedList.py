# Implement a function to calculate the sum of the numerical values in a nested list. 
# For example : sum_nested([1, [2, [3, [4]]]]) -> 10

def sum_nested(lst1):
    final_sum = 0
    for element in lst1:
        if type(element) == list:
            final_sum += sum_nested(element)
        else:
            final_sum += element
    return final_sum