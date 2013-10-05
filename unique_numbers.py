"""
Get an arbitrary array of numbers, extract and unique numbers out of it
"""

import random
import timeit


def unique_sorted(arr):
    """
    Returns the unique numbers from the given array
    The returned array is sorted
    """
    # sort the array
    arr.sort()

    # result array
    result = []

    for i, item in enumerate(arr):
        try:
            next_item = arr[i + 1]
        except:
            next_item = None

        if item != next_item:
            result.append(item)

    return result


def unique_unsorted(arr):
    """
    Returns the unique numbers from the given array
    The returned array is unsorted
    """
    # init an empty dict to store unique values
    hash_table = dict()
    result = []

    for item in arr:
        hash_table[item] = None

    for item in hash_table:
        result.append(item)

    # return the sorted list, this is not the requirement but helps on testing
    return result


test_numbers = [41, 53, 62, 41, 12, 5, 53, 5, 41]
test_expected = [5, 12, 41, 53, 62]
assert test_expected == unique_sorted(test_numbers)

test_numbers = [1, 41, 2, 1, 51, 41, 2]
test_expected = [1, 2, 41, 51]
assert test_expected == unique_sorted(test_numbers)


test_numbers = [41, 53, 62, 41, 12, 5, 53, 5, 41]
test_expected = [5, 12, 41, 53, 62]
assert test_expected == sorted(unique_unsorted(test_numbers))

test_numbers = [1, 41, 2, 1, 51, 41, 2]
test_expected = [1, 2, 41, 51]
assert test_expected == sorted(unique_unsorted(test_numbers))

print "all tests are passed"


"""
Print the total amount of execution time
unique_sorted:       28.7588908672
unique_unsorted:     23.3944420815
python sets:         21.6865098476
"""


def timeit_sorted():
    test_numbers = [random.randint(0, 10000) for r in xrange(10000)]
    unique_sorted(test_numbers)


def timeit_unsorted():
    test_numbers = [random.randint(0, 10000) for r in xrange(10000)]
    unique_unsorted(test_numbers)


def timeit_python_sets():
    test_numbers = [random.randint(0, 10000) for r in xrange(10000)]
    set(test_numbers)


print timeit.Timer('timeit_sorted()', 'from __main__ import timeit_sorted; import random').timeit(number=1000)
print timeit.Timer('timeit_unsorted()', 'from __main__ import timeit_unsorted; import random').timeit(number=1000)
print timeit.Timer('timeit_python_sets()', 'from __main__ import timeit_python_sets; import random').timeit(number=1000)
