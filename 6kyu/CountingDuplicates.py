# Write a function that will return the count of distinct case-insensitive a
# lphabetic characters and numeric digits that occur more than once in the input string. 
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    lowerText = text.lower()
    found = []
    for char in lowerText:
        if(not(char in found) and lowerText.count(char) > 1):
            found.append(char)
            
    return len(found)