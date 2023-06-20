def binary_search(arr, low, high, key):
    # searches for key in sorted arr and returns index of key through recursion method
    
    # CONQUER
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == key:
            return mid
        
        # DIVIDE
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, key)
 
    else:
        # Element is not present in the array
        return -1

# TIME COMPLEXITY = O(logN)
# SPACE COMPLEXITY = O(logN)

# Driver function
if __name__ == "__main__":
    a = [int(num) for num in input("Enter integer array in ascending order: ").split()]
    k = int(input("Enter search key: "))
    
    min_a, max_a = 0, len(a)-1
    idx = binary_search(a, min_a, max_a, k)   # binary search by recursion
    if idx != -1:
        print(k, "found in", idx+1, "position")
    else:
        print(k, "not found")
