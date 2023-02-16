import math

# Given distances in km
a = 1.35 # a -> b Sunset Resevoir to Golden Gate Hights Park
b = 5.8  # b -> c Golden Gate Hights Park to Herbert Hoover Middle
c = 5.7  # c -> b Herbert Hoover Middle to Sunset Resevoir

def CalcArea(a,b,c):
      # Calculate angles using Law of Cosines
      cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
      cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
      cos_C = (a**2 + b**2 - c**2) / (2 * a * b)

      A = math.degrees(math.acos(cos_A))
      B = math.degrees(math.acos(cos_B))
      C = math.degrees(math.acos(cos_C))

      # Calculate area using Law of Sines
      sin_A = math.sin(math.radians(A))
      sin_B = math.sin(math.radians(B))
      sin_C = math.sin(math.radians(C))

      # Use the Law of Sines to calculate the area of the triangle
      Area = 0.5 * a * b * sin_C
      return Area
            
def test_CalcArea():
    test_cases = [
        ((3, 4, 5), 6),
        ((1.35, 5.8, 5.7), 3.84),
        ((7, 8, 10), 24)
    ]

    for i, (input_values, expected_area) in enumerate(test_cases):
        try:
            result = CalcArea(*input_values)
            passed = math.isclose(result, expected_area, rel_tol=1e-2)
            status = "PASSED" if passed else "FAILED"
            print(f"Test {i}: {status}\nInput: {input_values}\nOutput: {result:.2f}\nOutput: {result:.2f}\nExpected: {expected_area}\n")
        except Exception as e:
            print(f"Test {i}: FAILED\nInput: {input_values}\nError: {str(e)}\n")

test_CalcArea()
