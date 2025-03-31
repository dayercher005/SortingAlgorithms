'''
Insertion sort is a simple sorting algorithm that builds the final sorted arrray one item at a time.

It sorts the array by inserting each element in to its current position. At any point, the left side of the array is sorted while the 
right side is unsorted. We choose the first element in the unsorted array and insert it into the unsorterd array in the correct position.
We then repear this process for the next element in the unsorted array.

It is much less efficient on large lists than more advanced algorithms such as quick sort, heap sort or merge sort.

Step 1: Start with the second element

Step 2: Compare and Shift

Step 3: Insert current element
'''

def insertion_sort(arr):
    for index in range(1, len(array)):
        key = array[index]
        j = index - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return array

# Time Complexity: O(n^2)
# Space Complexity: O(1)
