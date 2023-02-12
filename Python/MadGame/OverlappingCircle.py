# Python3 code to implement the approach ad 

from math import acos, sqrt

def intersection_area(d,r1,r2): # ans is in km^2
    d1 = (r1**2 - r2**2 + d**2) / (2 * d)
    d2 = d - d1
    area = (r1**2 * acos(d1/r1) - d1 * sqrt(r1**2 - d1**2)) + (r2**2 * acos(d2/r2) - d2 * sqrt(r2**2 - d2**2))
    return area




