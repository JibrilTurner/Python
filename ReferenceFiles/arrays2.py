import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

x = [64, 41, 3, 4, 7, 9]

for num in x:
    if is_prime(num):
        print(num, "is prime")
    else:
        print(num, "is not prime") 