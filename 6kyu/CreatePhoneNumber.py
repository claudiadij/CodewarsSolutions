# Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    s = "".join([str(i) for i in n])
    return f"({s[:3]}) {s[3:6]}-{s[6:]}"
