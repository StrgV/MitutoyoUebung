# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(check_for):
    length = len(str(check_for))
    for i in range(1, round(length / 2) + 1):
        if int(str(check_for)[i - 1]) != int(str(check_for)[-i]):
            return False
    return True


def find_all_palindromes_for_n_digits(digits: int) -> list:
    n1 = 10 ** digits - 1
    n2 = n1
    palindromes = []
    for i in range(n1, 0, -1):
        for j in range(n2, 0, -1):
            possible_palindrome = i * j
            if is_palindrome(possible_palindrome):
                if possible_palindrome not in palindromes:
                    palindromes.append(possible_palindrome)
    return palindromes


def find_largest_palindrome(digits: int):
    palindromes = find_all_palindromes_for_n_digits(digits)
    return max(palindromes)



assert is_palindrome(3663)
assert find_all_palindromes_for_n_digits(1) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
assert find_largest_palindrome(1) == 9

if __name__ == "__main__":
    print(find_largest_palindrome(3))
