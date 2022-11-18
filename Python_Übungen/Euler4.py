# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def calculate_and_check(index1: int, index2: int) -> int:
    check_for = index1 * index2
    length = len(str(check_for))
    for i in range(1, round(length/2) + 1):
        if int(str(check_for)[i - 1]) == int(str(check_for)[-i]):
            pass
        else:
            return 0
    return check_for
assert calculate_and_check(91, 99) == 9009
assert calculate_and_check(12, 12) == 0

def find_all_palindromes_for_n_digits(digits: int) -> list:
    n1 = 10 ** digits - 1
    n2 = n1
    palindromes = []
    for i in range(n1, 0, -1):
        for j in range(n2, 0, -1):
            possible_palindrome = calculate_and_check(i, j)
            if possible_palindrome != 0:
                palindromes.append(possible_palindrome)
    return palindromes
assert find_all_palindromes_for_n_digits(1) == [9, 8, 7, 6, 5, 8, 4, 9, 6, 3, 8, 6, 4, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def find_largest_palindrome(digits: int):
    palindromes = find_all_palindromes_for_n_digits(digits)
    return max(palindromes)
assert find_largest_palindrome(1) == 9
print(find_largest_palindrome(3))