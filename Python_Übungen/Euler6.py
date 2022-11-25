# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def find_sum_of_squares(maximum: int) -> int:
    result = 0
    for i in range(1, maximum + 1):
        result = result + i ** 2
    return result


def find_square_of_sums(maximum: int) -> int:
    result = 0
    for i in range(1, maximum + 1):
        result = result + i
    return result ** 2


def find_difference(maximum: int) -> int:
    return find_square_of_sums(maximum) - find_sum_of_squares(maximum)


assert find_difference(10) == 2640
assert find_square_of_sums(10) == 3025
assert find_sum_of_squares(10) == 385

print(find_difference(100))
