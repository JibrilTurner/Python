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
        (4, 4, "1x^3"),
        (3, 5, "15x^4"),
        (8, 8, "64x^7")
    ]

    for i, (base, exponent, expected) in enumerate(test_cases):
        try:
            result = differentiate(base, exponent)
            passed = result == expected
            status = "PASSED" if passed else "FAILED"
            print(f"Test {i}: {status}\nInput: Base = {base}, Exponent = {exponent}\nOutput: {result}\nExpected: {expected}\n")
        except Exception as e:
            print(f"Test {i}: FAILED\nInput: Base = {base}, Exponent = {exponent}\nError: {str(e)}\n")


    for i, (r1,r2,d, expected) in enumerate(test_cases):
        try:
            result = differentiate(base, exponent)
            passed = result == excepted
            status = "PASSED" if passed else "FAILED"
            print(f"Test {i}: {status}\nInput: R1 = {r1}, R2 = {r2}, D = {d}\nOutput: Area = {area}, D1 = {d1} , D2 = {d2}\nExpected: {expected}\nGot: {area}\n")
        except Exception as e:
            print(f"Test {i}: FAILED\nInput: R1 = {r1}, R2 = {r2}, D = {d}\nError: {str(e)}\n")
test_differentiate()
