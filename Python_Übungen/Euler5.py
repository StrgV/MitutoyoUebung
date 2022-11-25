# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_smallest_evenly_divisible_from_1_to_max(max: int) -> int:
    smallest_evenly_divisible = 2
    for i in range(1, max):
        if smallest_evenly_divisible % i != 0:
            smallest_evenly_divisible = smallest_evenly_divisible * find_smallest_multiplier(smallest_evenly_divisible, i)
    return smallest_evenly_divisible


def find_smallest_multiplier(factor: int, divisible_by: int) -> int:
    for smallest_multiplier in range(1, divisible_by + 1):
        if (factor * smallest_multiplier) % divisible_by == 0:
            return smallest_multiplier


print(find_smallest_evenly_divisible_from_1_to_max(20))
