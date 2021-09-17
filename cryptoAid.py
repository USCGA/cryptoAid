# Calculates prime using mod 2 division
def isPrime(val):
    return val % 2 == 1

# Calculates gcd using euclidean algorithm
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

# Calculates mod inverse
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modInverse(a, m):
    for x in range(1,m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
