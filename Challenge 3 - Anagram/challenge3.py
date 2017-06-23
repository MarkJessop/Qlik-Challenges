#!/usr/bin/env python3

# Date created: 2017-06-20
# Last modified: 2017-06-23
# Developer: Ashley Lesperance
#
# Description:  Qlik Programming Challenge 3
#               Devise an algorithm to determine if two strings of letters are anagrams.
#               An anagram is direct word switch or word play, the result of rearranging the letters of a word
#               or phrase to produce a new word or phrase, using all the original letters exactly once.
#
# Developer notes:  We run through each phrase once giving us a runtime of O(n)
#                   The python dictionary is NOT a hash_table though has underlying hash table implementation as of time of coding,
#                   though I used the variable name for conceptual purposes
#

def is_anagram(phrase1,phrase2):
    if len(phrase1) < 1 or len(phrase2) < 1:
        return "Please enter a valid string"
    # Strip and lowercase
    phrase1 = ("".join(phrase1.split())).lower()
    phrase2 = ("".join(phrase2.split())).lower()
    # Build hash table for phrase 1 (one pass)
    hash_table = dict()
    for char in phrase1:
        if char in hash_table:
            hash_table[char] = hash_table[char] + 1
        else:
            hash_table[char] = 1
    # Decrement counts to check if anagrams
    for char in phrase2:
        if char in hash_table:
            hash_table[char] = hash_table[char] - 1
            if hash_table[char] < 1:
                del hash_table[char]
        else:
            return False
    if len(hash_table) > 0:
        return False
    return True

if __name__ == "__main__":
    # Run main program
    print("----- Given Tests -----\n")
    print('is_anagram("Debit Card","Bad Credit")')
    print(str(is_anagram("Debit Card","Bad Credit")))
    print('is_anagram("Astronomer","Moon starer")')
    print(str(is_anagram("Astronomer","Moon starer")))
    print('is_anagram("These churn air","The Hurricanes")')
    print(str(is_anagram("These churn air","The Hurricanes")))
    print('is_anagram("Dormitory","Dirty rooms")')
    print(str(is_anagram("Dormitory","Dirty rooms")))
    print("\n----- Extra Tests -----\n")
    print('is_anagram("a","a")')
    print(str(is_anagram("a","a")))
    print('is_anagram("","a")')
    print(str(is_anagram("","a")))
    print('is_anagram("I can handle numbers 123","I can handle numbers 123")')
    print(str(is_anagram("I can handle numbers 123","I can handle numbers 123")))
    print('is_anagram("Ash\'s test for special characters: !@#$%^&*(","Ash\'s test for special characters: !@#$%^&*(")')
    print(str(is_anagram("Ash\'s test for special characters: !@#$%^&*(","Ash\'s test for special characters: !@#$%^&*(")))
