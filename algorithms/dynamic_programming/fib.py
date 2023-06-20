def calc_fib(n):
    # function calc_fib computes fibonacci values upto given input n (using dynamic programming concept)
    # time complexity = O(n), spcae complexity = O(n)

    fib = [0,1] # initialize list to store starting fibonacci values
    
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2]) # calulate fibonacci value and append to list
    
    return fib

# Driver program
if __name__ == "__main__":
    print(calc_fib(3))