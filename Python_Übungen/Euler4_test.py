import unittest
from Euler4 import *

class Euler4Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(3663), "3663 sollte ein Palindrom sein")
        self.assertFalse(is_palindrome(3665), "3665 sollte kein Palindrom sein")