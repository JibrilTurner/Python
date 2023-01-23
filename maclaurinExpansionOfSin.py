import math
def sigmaNotation(start,end,inc,x):
    sin = 0
    for n in range(start,end,inc): #Start End Inc
        sign = (-1)**n
        y=x*(0.01745329251) # 3.14 / 180 
        sin = sin + (y**(2.0*n+1))/math.factorial(2*n+1)*sign
    return sin   


def test1():

     test = [sigmaNotation(0,50,1,30),sigmaNotation(0,50,1,90),sigmaNotation(0,50,1,120,),sigmaNotation(0,50,1,0) ]
     solu = [0.499999999741665544,1.0,5,0.0]
     a = len(test)
     for x in range(0 ,a):
         if test[x] == solu[x]:
           print("Test %d Passed" % (x))
         else:
           print("Test %d Failed" % (x))


print("Index Of Sigma Cannot Go Above 50")#level of percison Max = 50 
indexOfSum = int(input("Enter the Index of Sigma:"))#level of percison Max = 50 
wholePointOfThisCalc = int(input("Enter the X -> sin(X):"))
print(sigmaNotation(0,indexOfSum,1,wholePointOfThisCalc))
