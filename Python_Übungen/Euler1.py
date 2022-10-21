#https://projecteuler.net/problem=1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def partial_sum(factor: int, maximum: int = 1000):
    result = 0
    multiples = 0
    while multiples < maximum:
        result = result + multiples
        multiples = multiples + factor
    return result


multiples_of_three_or_fives = partial_sum(3) + partial_sum(5) - partial_sum(15)

print(multiples_of_three_or_fives)
