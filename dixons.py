import math;
from cryptoAid import gcd;

n = int(input("Enter a value of n:\t"))
startPoint = int(input("Enter a start point:\t"))

# HARD CODED for 8 primes
instanceSet = {tuple([-1,-1,0,0,0,0,0,0,0,0])}
primes = [2,3,5,7,11,13,17,19]

def primefactors(x, n):

    # HARD CODED for 8 primes
    instances = [x,n,0,0,0,0,0,0,0,0]

    while(n % 2 == 0):
        instances[primes.index(2)+2] += 1
        n = n/2

    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i == 0):

            try:
                instances[primes.index(i)+2] += 1
                n = n/i
            except:
                #print()
                return
    if(n>2):
        try:
            instances[primes.index(n)+2] += 1
        except:
            #print()
            return

    instanceSet.add(tuple(instances))

def compare():
    for entry in instanceSet:
        for entry2 in instanceSet:
            tryIt = True
            # HARD CODED for 8 primes
            for x in range(2,10):
                if(tryIt):
                    #print(f"entry: {entry}")
                    #print(f"entry2: {entry2}")
                    #print(f"entry[{x}] {entry[x]} and entry2[{x}] {entry2[x]}")
                    if((entry[x] + entry2[x]) % 2 == 0):
                        #print("passes")
                        # arbitrary
                        tryIt = True
                    else:
                        #print("fails")
                        tryIt = False
            if(not entry == entry2 and tryIt):
                return entry,entry2
    return 0,0
x = startPoint
while(True):
    # X is x
    baseGuess = pow(x, 2, n)
    # print(x, end=' ')
    # print(baseGuess)
    primefactors(x, baseGuess)
    if(x > startPoint+1):
        #print(f"here at {x}")
        #print(instanceSet)
        try:
            # HARD CODED for 8 primes
            instanceSet.remove(tuple([-1,-1,0,0,0,0,0,0,0,0]))
        except:
            #print('oh well')
            z = 1
        firstList, secondList = compare()
        #print(firstList, secondList)
        if(not firstList == 0 and not secondList == 0):
            a = firstList[0] * secondList[0]
            # HARD CODED for 8 primes
            finalList = [0,0,0,0,0,0,0,0]
            #print("here")
            for i in range(2,len(firstList)):
                finalList[i-2] = firstList[i] + secondList[i]
            #print(f"Primes:\t\t{primes}")
            #print(f"Sum of primes:\t{finalList}")
            b = 1
            for i in range(len(finalList)):
                if(not primes[i] == 0):
                    b *= pow(primes[i], finalList[i]/2)
            check = gcd(abs(a-b), n)
            if(not check == n and not check == 1):
                print(f"a is: {a}, b is: {b}, gcd is: {check}")
                print(firstList, secondList)
                print(f"Primes:\t\t{primes}")
                print(f"Sum of primes:\t{finalList}")
                print(f"Factor: {check}")
                break
            else:
                z = 1
    x += 1
