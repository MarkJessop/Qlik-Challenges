#!/usr/bin/env python3

# Date created: 2017-06-18
# Last modified: 2017-06-23
# Developer: Ashley Lesperance
#
# Description:  Qlik Programming Challenge 1
#               Generate a list of 100 random integers between 1 and 99.
#               Write a program to sort this list, from lowest to highest, without using a language specific method that sorts a list for you
#
# Developer notes:  Input is a relatively small array with a small range, we can therefore trade off space efficiency for gains in time efficiency
#                   Average performance: O(n+k)

import random

def generate_random_list(count, minimum, maximum):
    # Genarate a list of $count random numbers with an inclusive range between $minimum and $maximum
    return [random.randint(minimum, maximum) for r in range(count)]

def bucket_sort_for_small_ranges(input_list, minimum, maximum):
    # Given the range is small, generate a bucket for each integer and sort in one pass
    number_of_lists = (maximum - minimum) + 1
    buckets = [[] for i in range(number_of_lists)]
    for i in range(len(input_list)):
        buckets[input_list[i]-minimum].append(input_list[i])
    sorted_list = []
    for bucket in buckets:
        sorted_list = sorted_list + bucket
    return sorted_list

def generate_and_sort(list_size, minimum, maximum):
    # Demonstrate the generation and sorting of lists
    random_list = generate_random_list(list_size, minimum, maximum)
    print("Generating list of length: " + str(list_size))
    #print("Generating list of length: " + str(len(random_list))) # Check actual length of list
    print("List before sorting:")
    print(random_list)
    print("List after sorting:")
    print(bucket_sort_for_small_ranges(random_list, minimum, maximum))


if __name__ == "__main__":
    # Run main program
    generate_and_sort(100,1,99)
