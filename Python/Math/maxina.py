import sympy #1.11.1
# Python 3.11.1

x = sympy.Symbol('x')

#funtion 


def findMaxOrMin(f):

    #Take the Derivative 
    first_derivative = sympy.diff(f, x)

    # Find the Inputs where f’(x) = 0 
    critical_points = sympy.solve(first_derivative)

    #Find the Maximum value
    maximum = sympy.Max(*[f.subs(x, critical_point) for critical_point in critical_points])

    #Find the Minimum value
    minimum = sympy.Min(*[f.subs(x, critical_point) for critical_point in critical_points])

    # #This means the local Minima occures Here
    # print("\nlocal Minima occures at :", critical_points[0])
    # #This means the local Y? occures Here
    # print("The maximum value is:", maximum)
    # #This means the local Maxima occures Here
    # print("\nlocal Maxima occures at :", critical_points[1])
    # #This means the local Y? occures Here
    # print("The minimum value is:", minimum)

    return critical_points[0] , maximum ,critical_points[1],minimum


def run_tests():
    functions = [(x**3 - 12*x + 1), (x / (x**2 + 1)),(x**3-3*x**2+1)]
    solutions = [(-2,17,2,-15),(-1,-1/2,1,1/2),(0,1,2,-3)]
    for i, (f, sol) in enumerate(zip(functions, solutions)):
        result = findMaxOrMin(f)
        passed = result == sol
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: {status}\nExpected: {sol}\nGot: {result}\n")
run_tests()

# f = x / (x**2 + 1)
# findMaxOrMin(f)