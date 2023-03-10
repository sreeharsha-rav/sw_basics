def merge_sort(arr):
    # sorts arr in ascending order via divide and conquer
    start = 0
    end = len(arr)

    if end == 1:
        sorted_arr = arr
        return sorted_arr
    
    mid = (start + end) // 2
    left = arr[start : mid]
    right = arr[mid : end]

    left = merge_sort(left)    # divide
    right = merge_sort(right)   # divide
    sorted_arr = merge(arr, left, right) # combine

    return sorted_arr


def merge(arr, left, right):
    # combines left and right arrays and sorts them into arr

    i = j = k = 0   # indices to track combining

    while (i < len(left)) and (j < len(right)): # copy smallest uncombined elements into arr
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
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
