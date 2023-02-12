def differentiate(base, exponent):
    if exponent == base:
        return "0"
    else:
        result = exponent * base
        exponent = exponent - 1 
        if base < 0 or exponent < 0:
            result = "-" + str(abs(result))
        else:
            result = str(result)
        return result + "x^" + str(abs(exponent))
        
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# result = differentiate(base, exponent)
# print(*result, sep="")

def test_differentiate():
    test_cases = [
        (15, 2, "30x^1"),
        (37, 4, "148x^3"),
        (4,  8, "32x^7")
    ]

    for i, (base, exponent, expected) in enumerate(test_cases):
        try:
            result = differentiate(base, exponent)
            passed = result == expected
            status = "PASSED" if passed else "FAILED"
            print(f"Test {i}: {status}\nInput: Base = {base}, Exponent = {exponent}\nOutput: Base = {base*exponent}, Exponent= {exponent-1}\nExpected: {expected}\nGot: {result}\n")
        except Exception as e:
            print(f"Test {i}: FAILED\nInput: Base = {base}, Exponent = {exponent}\nError: {str(e)}\n")

test_differentiate()