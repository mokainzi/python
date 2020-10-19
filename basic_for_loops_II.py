# Biggie Size
# Given a list, write a function that changes all positive
# numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values
# are now [-1, "big", "big", -5]
def biggie_size(alist) :
    for i in range(len(alist)):
        if alist[i] > 0:
            alist[i] = "big"
    return alist

biggie_size([-1, 3, 5, -5])


# Count Positives
# Given a list of numbers, create a function to replace the
# last value with the number of positive values. (Note that zero is not
# considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list
# to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list
# to [1,6,-4,-2,-7,2] and returns it
def count_positives(alist):
    positives_count = 0
    for i in range(len(alist)):
        if alist[i] > 0:
            positives_count += 1
    alist[-1] = positives_count
    print(alist)

#count_positives([-1,1,1,1])
count_positives([1,6,-4,-2,-7,-2])


# Sum Total
# Create a function that takes a list and returns the sum of all
# the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(alist):
    array_sum = 0
    for i in range(len(alist)):
        array_sum += alist[i]
    return array_sum

sum_total([1,2,3,4])
sum_total([6,3,-2])


# Average
# Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(alist):
    list_sum = 0
    for i in range(len(alist)):
        list_sum += alist[i]
    return list_sum/len(alist)

average([1,2,3,4])


# Length
# Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(alist):
    count = 0
    for i in alist:
        count += 1
    return count

length([37,2,1,-9])
length([])


# Minimum
# Create a function that takes a list of numbers and returns the minimum value
# in the list. (Optional) If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# (Optional) Example: minimum([]) should return False
def minimum(alist):
    count = 0
    min_val = 2e99
    for i in alist:
        count += 1
        if i < min_val:
            min_val = i
    if count == 0:
        return False
    else:
        return min_val

minimum([37,2,1,-9])
minimum([])


# Maximum
# Create a function that takes a list and returns the maximum value in the array.
# (Optional) If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# (Optional) Example: maximum([]) should return False
def maximum(alist):
    count = 0
    max_val = -2e99
    for i in alist:
        count += 1
        if i > max_val:
            max_val = i
    if count == 0:
        return False
    else:
        return max_val

maximum([37,2,1,-9])
maximum([])
