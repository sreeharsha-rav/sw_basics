def selection_sort(arr):
    # sorts input array in ascending order
    
    for i in range(len(arr)):
        # starting with leftmost element
        min_idx = i 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swap leftmost element with min element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# driver code
if __name__ == "__main__":
    num_list = [int(num) for num in input("Enter integer array: ").split()]
    sort_list = selection_sort(num_list)
    print("Sorted array: ", sort_list)
