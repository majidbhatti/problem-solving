def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Element found, return its index.
        elif mid_element > target:
            high = mid - 1  # Target is in the left half.
            mid = high+1
        else:
            low = mid + 1   # Target is in the right half.
            mid = low

    return mid  # Element not found.


if __name__ =='__main__':
    print(binary_search([1,3,4,6],2))
