''' Implementation of binary and linear search '''

def linear_search(arr, element):
    for idx, val in enumerate(arr):
        if element == val:
            return idx

    # by default return -1 if element not found
    return -1

def binary_search(arr, element):
    left_idx = 0
    right_idx = len(arr) - 1

    mid_idx = left_idx + right_idx // 2

    while left_idx < right_idx:
        if element < arr[mid_idx]:
            right_idx = mid_idx - 1

        elif element > arr[mid_idx]:
            left_idx =  mid_idx + 1

        if element == arr[mid_idx]:
            return mid_idx

    # return -1 if element not present
    return -1

def binary_search_recursive(arr, element, left_idx, right_idx):
    if left_idx > right_idx:
        return -1

    mid_idx = (left_idx + right_idx) // 2

    while mid_idx < len(arr) or mid_idx >= 0:
        if arr[mid_idx] == element:
            return mid_idx

        if element < arr[mid_idx]:
            right_idx = mid_idx -1

        if element > arr[mid_idx]:
            left_idx = mid_idx +1

        binary_search_recursive(arr, element, left_idx, right_idx)

if __name__=="__main__":
    # sample sorted array
    arr = [2, 3, 5, 7, 9, 22]

    # element to search
    element = 5

    # by linear search
    print(f"Element present at {linear_search(arr, element)} index.")

    # by binary search
    print(f"Element present at {binary_search(arr, element)} index.")

    # by binary recursive search
    print(f"Element present at {binary_search_recursive(arr, element, left_idx = 0, right_idx = len(arr)-1)} index.")

