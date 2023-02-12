import math
def sigmaNotation(start,end,inc):
    sum = 0 
    for n in range(start,end,inc): #Start End Inc
        solu = 2*n # eqution 
        sum = sum + solu # sum
    return sum
print(sigmaNotation(1,3,1))