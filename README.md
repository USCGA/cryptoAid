# CryptoAid

CryptoAid is a collection of python scripts (some custom, some borrowed with love from the internet) that are useful in hands-on cryptography. This library is designed to be implemented and referenced in scripts for competitions, projects, and anything else! Please note that some of the work in this repository is the original work of various team members, and should not be considered online material for purposes of academic integrity at CGA.

## Installation

The intended use of this repository is to clone it to a local source, then call the python methods either in a live editor or in your own scripts.

```git
git clone https://github.com/USCGA/cryptoAid.git
cd cryptoAid
```

### Live Editor

Launch python and import the scripts:

```python3
>>> from cryptoAid import *
is_coprime, gcd, modInverse, totient, primRoots, bigLittleLog, solvePrimRoot, primeFactors
>>> totient(10)
4
>>>
```

### Import Into Scripts

Create a python file and import the file with your other import statements

```python
#!/usr/bin/python3

from cryptoAid import *

value = int(input('Enter the number to check:\t'))
print(f'Totient of {value} is {totient(value)}')
```

## Scripts

### cryptoAid.py

Currently, there are *eight* python methods in this file, all of which can be imported and used.

| Method Name | Method Function |
| :------------- | :------------- |
| is_coprime(x,y) | Tests if two numbers are coprime |
| is_gcd(x,y) | Returns the gcd of two numbers |
| modInverse(a,m) | Returns the modular inverse of a mod(m), or -1 if it does not exist |
| totient(x) | returns the Euler's Totient of x |
| primRoots(m) | returns a list of all primitive roots of a modular base m (gets slow for very large values of m) |
| solvePrimRoot(p,m) | Tests if a specific prime p is a primitive root of modular base m |
| bitLittleLog(a,c,p,n) | Attempts to factor a discrete logorithm using the baby step giant step algorithm |
| primtFactors(n) | Brute forces the prime factorization of n (gets very slow for large values of n) |

### dixons.py

This script attempts to find a factor of a number using [Dixon's algorithm](https://en.wikipedia.org/wiki/Dixon%27s_factorization_method). Certain parts of this method are hard coded for now, so shoot over a pull request with updates with a more customizable script!
