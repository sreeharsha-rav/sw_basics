def quick_sort(arr, left, right):
    # sorts arr in ascending order in place, through quicksort algorithm. Left - lowest index, Right - highest index

    if left >= right:   # number of elements is 1, then arr is already sorted
        return
    else:
        # CONQUER
        pivot_idx = partition(arr, left, right) # get pivot index
        # DIVIDE
        quick_sort(arr, left, pivot_idx-1)    # sort arr elements less than pivot
        quick_sort(arr, pivot_idx+1, right)   # sort arr elements greater than pivot

def partition(arr, left, right):
    # places smaller elements to left of pivot and greater elements to right of pivot, and return position of pivot
    
    pivot = arr[left]   # take left-most element as the pivot
    i = right + 1    # tracker for position where all elements are greater than pivot
    j = right   # variable for iterating through arr

    while j > left:
        if arr[j] >= pivot:
            i -= 1  # move tracker towards left
            arr[i], arr[j] = arr[j], arr[i] # swap to position elements greater than pivot on right-side of pivot
        j -= 1  # move index towards left
    
    arr[i-1], arr[left] = arr[left], arr[i-1]   # swap positions of pivot and element at pivot index

    return i-1


# Driver program
if __name__ == "__main__":
    a = [int(num) for num in input("Enter integer array to be sorted: ").split()]
    quick_sort(a, 0, len(a)-1)
    print("sorted array = ", a)