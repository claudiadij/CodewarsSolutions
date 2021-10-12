# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor

def divisible_by(numbers, divisor):
    return [i for i in numbers if i%divisor==0]