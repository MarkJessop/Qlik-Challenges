#!/usr/bin/env python3

# Date created: 2017-06-20
# Last modified: 2017-06-23
# Developer: Ashley Lesperance
#
# Description:  Qlik Programming Challenge 2
#               A palindromic number reads the same both ways.
#               The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#               Find the largest palindrome made from the product of two 3-digit numbers.
#
# Developer notes:  Runs with a worst case of O(n^2), but optimizations make it very unlikely to reach worst case
#                   The algorithm has been written for general purpose and can be used to find other palindromes of other multiplier lengths
#

def is_palindrome(possible_palindrome):
    # Checks if number is palindrome by reversing the string and comparing
    number_string = str(possible_palindrome)
    reverse_string = number_string[::-1] 
    if number_string == reverse_string:
        return True
    return False

def find_largest_palindromic_product(digits):
    # Given the digits of multipliers find the largest palindromic number
    nine = '9'
    one = '1'
    zero = '0'
    ceiling = int(nine*digits)
    floor = int(nine*(digits-1))
    largest_palindrome = int(one + zero*((digits*2)-2) + one)
    for i in range(ceiling, floor, -1):
        # skip if smaller than largest palindrome
        if i*ceiling < largest_palindrome:
            continue
        for j in range(ceiling, i, -1):
            product = i * j
            if product > largest_palindrome and is_palindrome(product):
                largest_palindrome = product
                largest_i = i
                largest_j = j
    return str(largest_palindrome) + "=" + str(largest_i) + "x" + str(largest_j)

if __name__ == "__main__":
    # Run main program
    print(find_largest_palindromic_product(3))
