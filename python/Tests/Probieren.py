from numpy import *


def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(sqrt(number) + 1), 2):
            if number % i == 0:
                return False
        return True
    return False


def getPrimeFactors(number):
    factors = []
    if isPrime(number):
        return number
    poss_primes = []
    for j in range(1, number):
        poss_primes.append(j) if isPrime(j) else None
    for i in poss_primes:
        factors.append(i) if number % i == 0 else None
    return factors


print(isPrime(8021658347))
