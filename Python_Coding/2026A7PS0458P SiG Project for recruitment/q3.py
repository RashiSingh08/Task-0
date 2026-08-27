# This is slightly hard. like, I could divide using all numbers till N/2 but that seems too inefficient...

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n%i == 0:
            break
    else:
        return True
    return False

#Instead of going from 2 to N/2, we go from 2 to rootN. Like, after that factors are just N/beforewalefactors
#Like if n = 1000, we aint checking more than 31. 

def all_primes(N):
    primes = []
    for i in range (2, N):
        if is_prime(n):
            all_primes.append(i)

n = int(input("Enter a number for checking if it's prime or not: "))
N = int(input("Enter a number for generating all primes till that number: "))