def insertion_sort(arr):
    # sorts input array in ascending order
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # shift all elements towards right to insert key
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key  # insert key
    
    return arr 

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(N)

# Driver code
if __name__ == "__main__":
    num_list = [int(num) for num in input("Enter integer array: ").split()]
    sort_list = insertion_sort(num_list)
    print("Sorted array: ", sort_list)
