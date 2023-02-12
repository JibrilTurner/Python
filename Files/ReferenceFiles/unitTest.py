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



def gptAdd(num1, num2):
    return num1 + num2

def test1():
  tests = [gptAdd(2, 2), gptAdd(5, 8)]
  solutions = [4, 13]
  n = len(solutions)
  for i in range(n):
    result = "Passed" if tests[i] == solutions[i] else "Failed"
    print(f"Test {i} {result}")

test1()