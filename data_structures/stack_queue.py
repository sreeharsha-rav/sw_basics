def stack_demo():
    # demo the funcitonality of stack with simple push and pop, using list
    stack = list()  # declare an empty stack

    # pushing items into stack
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("stack after pushing 1, 2 and 3 = ", stack)

    # popping an item from stack
    item = stack.pop()  # LIFO, pop last item
    print("pop item = ", item)
    print("stack after popping an item = ", stack)

def queue_demo():
    # demo the functionality of queue with put and get, using list
    queue = list()

    # put items into queue
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print("queue after putting a, b, c = ", queue)

    # get an item from queue
    item = queue.pop(0) # FIFO, get 1st item
    print("get item = ", item)
    print("queue after getting an item = ", queue)

# Driver Program
if __name__ == "__main__":
    stack_demo()    # demo stack
    queue_demo()    # demo queue