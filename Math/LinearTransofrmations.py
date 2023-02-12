def MatrixMultiplyer(Li,Lj,v):
    a = v[0] * Li[0] if type(v[0]) == int else v[0] + "" + str(Li[0]) 
    b = v[1] * Lj[0] if type(v[1]) == int else v[1] + "" + str(Lj[0]) 

    c = v[0] * Li[1] if type(v[0]) == int else v[0] + "" + str(Li[1]) 
    d = v[1] * Lj[1] if type(v[1]) == int else v[1] + "" + str(Lj[1]) 


    Top = (a+b)
    Bottom = (c+d)
    
    return Top, Bottom 

def test_MatrixMultiplyer():
    test_cases = [  ((3, -2), (-1,0), (5,-2), (17,-10)),   
                    ((1, -2), (3,0), (-1,2), (5,2)),  
                    ((1, -2), (3,1), ("x","y"), ("1x + 3y", "-2x + 0y"))    ]
    for i, (Li, Lj, v, expected) in enumerate(test_cases):
        result = MatrixMultiplyer(Li, Lj, v)
        passed = result == expected
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: {status}\nExpected: {expected}\nGot: {result}\n")

test_MatrixMultiplyer()