# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143
from math import sqrt

def find_all_prime_factor(n :int):

    primefactor = 3
    primefactors_of_n = []
    while True:
        if check_num_is_prime(primefactor):
            if (n % primefactor) == 0:
                primefactors_of_n.append(primefactor)
                n = n // primefactor
                if check_num_is_prime(n):
                    primefactors_of_n.append(n)
                    return primefactors_of_n
            else:
                primefactor = primefactor + 2
        else:
            primefactor = primefactor + 2


def check_num_is_prime(n :int):
    if n > 1:
        for i in range(2, int(sqrt(n))):
            if (n % i) == 0:
                return False
        return True



print(max(find_prime_factor(600851475143)))








