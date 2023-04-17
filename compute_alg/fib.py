def calc_fib1(n):
    # function calc_fib1 computes fibonacci values upto given input n (using dynamic programming concept)
    # time complexity = O(n), spcae complexity = O(n)

    fib = [0,1] # initialize empty list to store fibonacci values

    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# Driver program
if __name__ == "__main__":
    print(calc_fib1(10))