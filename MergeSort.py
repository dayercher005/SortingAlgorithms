''' 
Merge Sort is a divide and conquer algorithm that divides the input array into 2 halves, calls
itself for the two halves, and then merges the two sorted halves.

Step 1: Split array into halves

Step 2: Merge sorted halves
'''

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(arr[::mid])
    right = merge_sort(arr[mid::])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
