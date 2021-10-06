# Your task is to sort a given string. 
# Each word in the string will contain a single number. 
# This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. T
# The words in the input String will only contain valid consecutive numbers.

def order(sentence):
    words = []
    for i in range(1,10):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
    return " ".join(words)