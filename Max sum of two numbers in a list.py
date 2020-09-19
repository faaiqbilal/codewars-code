def maxSumOfTwoInAnArray(arr):
    # create set with no repeating integers
    # convert the list to a set so that it removes repeating units
    set_values = set(arr)
    # convert the newly created set back to list form
    list_sequence = sorted(list(set_values))

    print(list_sequence)
    # condition if all members are negative
    total = 0
    if all(list_sequence[x] < 0 for x in list_sequence):
        print("all members of the list are negative")
        return total
    # for any other case we add all the members of the list to each other

    else:
        return list_sequence[-1] + list_sequence[-2]


print(maxSumOfTwoInAnArray([2, 1, 3, 4, 1, 2, 1, 5, 4]))
print(maxSumOfTwoInAnArray([-1, -2, -3]))
print(maxSumOfTwoInAnArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
