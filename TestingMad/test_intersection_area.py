import test_Nuke

def test_intersection_area():
    test_cases = [
        (4, 4, 4, 19.65),
        (3, 5, 4, 18.22),
        (8, 8, 8, 201.06)
    ]

    for i, (r1,r2,d, expected) in enumerate(test_cases):
        try:
            area, d1, d2 = test_Nuke.intersection_area(r1, r2,d)
            passed = round(area, 2) == round(expected, 2)
            status = "PASSED" if passed else "FAILED"
            print(f"Test {i}: {status}\nInput: R1 = {r1}, R2 = {r2}, D = {d}\nOutput: Area = {area}, D1 = {d1} , D2 = {d2}\nExpected: {expected}\nGot: {area}\nGot: {passed}\n\n")
        except Exception as e:
            print(f"Test {i}: FAILED\nInput: R1 = {r1}, R2 = {r2}, D = {d}\nError: {str(e)}\n")

test_intersection_area()
