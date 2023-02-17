def binary_search(arr, key):
    # searches for key in sorted arr and returns index of key
    
    min_idx = 0
    max_idx = len(arr) - 1

    while min_idx != max_idx:
        mid_idx = (min_idx + max_idx) // 2
        
        if key == arr[mid_idx]:
            return mid_idx
        elif key > arr[mid_idx]:
            min_idx = mid_idx + 1
        else:
            max_idx = mid_idx - 1

    # checking when key is located either at min_idx or max_idx
    if key == arr[min_idx]:
        return min_idx
    else:
        return -1

# Driver function
if __name__ == "__main__":
    a = [int(num) for num in input("Enter integer array in ascending order: ").split()]
    k = int(input("Enter search key: "))
    
    # index of search key
    idx = binary_search(a,k)
    if idx != -1:
        print(k, "found in", idx+1, "position")
    else:
        print(k, "not found")
