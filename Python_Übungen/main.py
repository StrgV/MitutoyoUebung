def partial_sum(factor: int, maximum: int = 1000):
    result = 0
    multiples = 0
    while multiples < maximum:
        result = result + multiples
        multiples = multiples + factor
    return result


multiples_of_three_or_fives = partial_sum(3) + partial_sum(5) - partial_sum(15)

print(multiples_of_three_or_fives)
