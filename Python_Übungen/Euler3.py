# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143
from math import sqrt


def find_prime_factor(n: int) -> list:
    primefactors_of_n = []
    n = append_primefactors(n, 2, primefactors_of_n)
    prime_factor = 3
    while not check_num_is_prime(n):
        n = append_primefactors(n, prime_factor, primefactors_of_n)
        prime_factor = prime_factor + 2
    primefactors_of_n.append(n)
    return primefactors_of_n


def append_primefactors(n: int, prime_factor: int, primefactors_of_n: list) -> int:
    while (n % prime_factor) == 0:
        primefactors_of_n.append(prime_factor)
        n = n // prime_factor
    return n


def check_num_is_prime(n: int) -> bool:
    if n > 1:
        for i in range(2, int(sqrt(n))):
            if (n % i) == 0:
                return False
        return True


print(max(find_prime_factor(600851475143)))
