def fibonacci(num):
    # compute the fibonacci number at num
    if num < 0:
        raise ValueError("Input number is below 0")
    
    if num < 2:    # fibonacci 0 = 0, fibonacci 1 = 1
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)  # sum of 2 preceding numbers

# TIME COMPLEXITY = O(2^N)
# SPACE COMPLEXITY = O(N)
 
# Driver Program
if  __name__ == "__main__":
    n = int(input("Enter an integer number to find nth fibonacci number: "))
    print("fibonacci number at {0} = {1}".format(n, fibonacci(n)))