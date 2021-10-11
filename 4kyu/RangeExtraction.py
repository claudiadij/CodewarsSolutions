# A format for expressing an ordered list of integers is to use a comma separated
# list of either individual integers or a range of integers denoted by the starting 
# integer separated from the end integer in the range by a dash, '-'. 
# The range includes all integers in the interval including both endpoints. 
# It is not considered a range unless it spans at least 3 numbers. 
# For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order 
# and returns a correctly formatted string in the range format.

def solution(args):
    output = ''
    consecutive = []
    for num in args:
        if consecutive:
            if consecutive[-1] == num-1:
                consecutive.append(num)
            else:
                if len(consecutive)>=3:
                    next = f'{consecutive[0]}-{consecutive[-1]}'
                    output += next+','
                else:
                    for prev in consecutive:
                        output+=str(prev)+','
                consecutive = []
                consecutive.append(num)
            if num == args[-1]:
                if len(consecutive)>=3:
                    next=f'{consecutive[0]}-{consecutive[-1]}'
                    output += next
                else:
                    for prev in consecutive:
                        output+=str(prev)+','
        else:
            consecutive.append(num)

    return output.rstrip(',')