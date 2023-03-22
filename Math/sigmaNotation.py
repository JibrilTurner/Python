import math

def sigmaNotation(start, end, inc):
    end = end + 1
    sum = 0

    for n in range(start, end, inc):
        solu = (3/2)**n - 1
        sum = sum + solu

    return sum

print(sigmaNotation(1, 4, 1))