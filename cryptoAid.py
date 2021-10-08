def is_coprime(x, y):
    return gcd(x, y) == 1

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

def totient(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)

def primRoots(modulo):
    required_set = {num for num in range(1, modulo) if gcd(num, modulo) }
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]


print("is_coprime, gcd, modInverse, totient, primRoots")
