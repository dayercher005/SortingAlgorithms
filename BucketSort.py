'''
Bucket Sort is a sorting alogirthm that distributes the elements of an array into several groups, called
buckets. Each bucket is then sorted individually, either using a different sorting algorithm or by recursively
applying the bucket sorting algorithm.

Step 1: Create Buckets

Step 2: Sort Buckets
'''

def bucket_sort(array):
    if not array:
        return array

    # Find range of values
    max_value, min_value = max(array), min(array)

    # Create buckets
    bucket_range = (max_value - min_value) / len(array)
    buckets = [[] for _ in range(len(array) + 1)]

    # Distribute input array values into buckets
    for i in array:
        if i == max_value:
            bucket_idx = len(array) - 1
        else:
            bucket_idx = int((i - min_value) / bucket_range)
        buckets[bucket_idx].append(i)

    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()

    # Concatenate all buckets into final array
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

# Time Complexity: O(n)
# Space Complexity: O(n + k), where k is the number of buckets
