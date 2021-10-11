# Initially a number 1 is written on a board. It is possible to do the following operations with it:

# multiply the number by 3; increase the number by 5. Your task is to determine that using this two operations step by step, is it possible to obtain number n?

def number_increasing(n):
    if n == 1:
        return True
    if (n - 1) % 5 == 0:
        return True
    t = 3
    while t <= n:
        if t == n or (n - t) % 5 == 0:
            return True
        t *= 3
    return False