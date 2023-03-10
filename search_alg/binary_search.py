def binary_search1(arr, key):
    # searches for key in sorted arr and returns index of key through iteration method
    
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
    
def binary_search2(arr, low, high, key):
    # searches for key in sorted arr and returns index of key through recursion method
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == key:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > key:
            return binary_search2(arr, low, mid - 1, key)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search2(arr, mid + 1, high, key)
 
    else:
        # Element is not present in the array
        return -1

# Driver function
if __name__ == "__main__":
    a = [int(num) for num in input("Enter integer array in ascending order: ").split()]
    k = int(input("Enter search key: "))
    
    # index of search key
    idx = binary_search1(a,k)   # binary search by iteration
    if idx != -1:
        print(k, "found in", idx+1, "position")
    else:
        print(k, "not found")
    
    min_a, max_a = 0, len(a)-1
    idx = binary_search2(a, min_a, max_a, k)   # binary search by recursion
    if idx != -1:
        print(k, "found in", idx+1, "position")
    else:
        print(k, "not found")
