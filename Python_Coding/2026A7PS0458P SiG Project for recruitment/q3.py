# This is slightly hard. like, I could divide using all numbers till N/2 but that seems too inefficient...

def is_prime(n):
    if n <= 1:
        pp = ("Number is less than 1!!")
        return False
        
    for i in range(2, int(n**0.5) +1):
        if n%i == 0:
            pp = ("Number is composite")
            break
    else:
        pp = ("Number is prime")
        return True
    return False

#Instead of going from 2 to N/2, we go from 2 to rootN. Like, after that factors are just N/beforewalefactors
#Like if n = 1000, we aint checking more than 31. 

def all_primes(N):
    primes = []
    for i in range (2, N+1):
        if is_prime(i):
            primes.append(i)
    return primes

n = int(input("Enter a number for checking if it's prime or not: "))
if is_prime(n):
    print(f"{n} is prime")
else:
    if n<=1:
        print(f"{n} is less than 1")
    else: 
        print(f"{n} is composite")

N = int(input("Enter a number for generating all primes till that number: "))
print(*all_primes(N))