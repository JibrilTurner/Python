import math
def add(num1,num2):
  sum = num1+num2
  return sum   

def test1():
    test = [add(2,2),add(5,8)]
    solu = [4,9]
    x = len(solu)
    print(x)
    for x in range(0 ,x):
        if test[x] == solu[x]:
          print("Test %d Passed ✔ " % (x))
        else:
         print("Test %d Failed ✖" % (x))

         
print(test1())