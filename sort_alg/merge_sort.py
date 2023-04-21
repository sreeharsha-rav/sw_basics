def merge_sort(arr):
    # sorts arr in ascending order via divide and conquer -> merge sort
    start = 0
    end = len(arr)

    if end == 1:    # if number of elements is 1, then arr is already sorted
        sorted_arr = arr
        return sorted_arr
    
    # DIVIDE
    mid = (start + end) // 2    # calculate mid and divide into left and right arrays
    left = arr[start : mid]
    right = arr[mid : end]
    
    # CONQUER
    left = merge_sort(left)
    right = merge_sort(right)
    
    # COMBINE
    sorted_arr = merge(arr, left, right)

    return sorted_arr


def merge(arr, left, right):
    # takes elements from left and right, puts them into arr while sorting simultaneously

    i = j = k = 0   # indices to track combining, i for left, j for right and k for merged arr

    while (i < len(left)) and (j < len(right)): # copy smallest uncombined elements into arr
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1  # increment left index
        else:
            arr[k] = right[j]
            j += 1  # increment right index
        k += 1  # increment merged arr index
    
    while i < len(left):    # copy left-over left elements into arr
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):   # copy left-over right elements into arr
        arr[k] = right[j]
        j += 1
        k += 1
    
    return arr

# Driver Code
if __name__ == "__main__":
    a = [int(num) for num in input("Enter integer array to be sorted: ").split()]

    sorted_a = merge_sort(a)
    print("sorted array = ", sorted_a)
