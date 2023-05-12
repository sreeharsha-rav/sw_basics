def factorial(num):
    # compute the factorial of num

    if num == 0:    # 0! is 1
        return 1
    else:
        return num * factorial(num-1)   # n! = n*(n-1)*(n-2)*....*1
    
# TIME COMPLEXITY = O(N)
 
# Driver Program
if  __name__ == "__main__":
    n = int(input("Enter an integer number to compute factorial: "))
    print("Factorial = ", factorial(n))