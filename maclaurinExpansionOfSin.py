import math
def sigmaNotation(start,end,inc,x):
    sin = 0
    for n in range(start,end,inc): #Start End Inc
        sign = (-1)**n
        y=x*(0.01745329251) # 3.14 / 180 
        sin = sin + (y**(2.0*n+1))/math.factorial(2*n+1)*sign
    return sin   

print("Index Of Sigma Cannot Go Above 50")#level of percison Max = 50 
indexOfSum = int(input("Enter the Index of Sigma:"))#level of percison Max = 50 
wholePointOfThisCalc = int(input("Enter the X -> sin(X):"))
print(sigmaNotation(0,indexOfSum,1,wholePointOfThisCalc))
