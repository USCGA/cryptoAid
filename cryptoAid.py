import math

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

def bigLittleLog(a,c,p,num_steps):
    # y ~= log base 28 of 74 (mod 257)
    # X != log base a of c (mod p)

    # a = 28
    # c = 74
    # p = 257

    N = math.floor(pow(p-1,0.5)) + 1
    print(N)

    a_inverse = modInverse(a,p)
    print(a_inverse)

    a_negN = pow(a_inverse, N, p)
    print(a_negN)

    big_steps = [0]*num_steps
    little_steps = [0]*num_steps

    print("\nLittle:\tBig:")
    for x in range(num_steps):
        little_steps[x] = pow(a,x,p)
        big_steps[x] = (c * pow(a_negN,x)) % p

        print(f"{little_steps[x]}\t{big_steps[x]}")

        if(little_steps[x] in big_steps):
            print("Match found!")
            j = x
            k = big_steps.index(little_steps[x])
            break
        elif(big_steps[x] in little_steps):
            print("Match found!")
            k = x
            j = little_steps.index(big_steps[x])
            break
    solution = j + k * N
    return solution


print("is_coprime, gcd, modInverse, totient, primRoots, bigLittleLog")
