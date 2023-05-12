## Recursion

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems. It consists of 2 main parts: Base Case and Recursion Cue.

- _Base Case_: Condition that stops the recursive function from recursing indefinitely.
- _Recursion Cue_: Cue to call the recursive function with an input that gets it closer to the base case.

A call stack is used to store the invocations of recursive functions. As a stack follow LIFO, the last function in it's stack is when the base case is met.

**Cons**
- If the base case is not met it leads to stack overflow error. This would also happen if the call stack is limited in size and the number of recursive calls are huge, as it will not be able to accomodate all recursive function calls.
- If the base case is not defined properly, it would lead the recursive function to run indefinitely.
- Less efficient than comparable iterative solutions due to call stack.

**Pros**
- Reduces complex problems to a simple solution using few lines of code.

### Recursive Algorithms

**factorial**

Compute the factorial of a given positive integer. A factorial is a mathematical function that computes the product of all positive integers upto given input numer. For example, fatorial of 5 is _5! = 5*4*3*2*1_.
- Time Complexity = O(N)

*This is good for recursion.*

**fibonacci**

Compute the nth fibonacci number for given input. A fibonacci sequence is a sequence of numbers where each number is the sum of 2 preceding numbers and the nth fibonacci number would be the nth number in this sequence. For example, 7th fibonacci number is _8_ and the corresponding fibonacci sequence is _0, 1, 1, 2, 3, 5, 8_.
- Time Complexity = O(2^N)

*This is not good for recursion.*
