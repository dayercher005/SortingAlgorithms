'''
Quick sort is a divide and conquer algorithm that picks an element as pivot and partitions the given array
around the picked pivot.

Unlike merge sort, quick sort is not a stable sort. This means that the input order of equal elements in 
the sorted output may not be preserved.

Step 1: Partition the array

Step 2: Recursively sort subarrays.
'''

def quick_sort(array):
    if len(array) <= 1:
            return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Time Complexity: O(nlogn)
# Space Complexity: O(logn)
