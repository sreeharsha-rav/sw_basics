def bubble_sort(arr):
    # sorts input array in ascending order
    for i in range(len(arr)):
        # last i elements would have already been sorted
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                # swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)

# driver code
if __name__ == "__main__":
    num_list = [int(num) for num in input("Enter integer array: ").split()]
    sort_list = bubble_sort(num_list)
    print("Sorted array: ", sort_list)
