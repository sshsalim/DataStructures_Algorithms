''' Implementation of bubble sort in python'''

def bubble_sort(arr):

    for i in range(0, len(arr) -1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j + 1] = temp

    return arr

if __name__ == "__main__":
    # default array
    arr = [3, 1, 7, 4, 2, 5, 0]

    # sorted array
    print(f"The sorted array: {bubble_sort(arr)}" )



