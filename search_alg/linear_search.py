def linear_search(arr, key):
    # searches for key in arr and returns index of key
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1

# Driver Code
if __name__ == "__main__":
    # input a list
    a = [num for num in input("Enter a list of elements: ").split()]
    # input a search key
    k = input("Enter search element: ")
    # get index of search key
    idx = linear_search(a, k)
    if idx != -1:
        print(k, "found in", idx+1,"position")
    else:
        print(k, "not found")
