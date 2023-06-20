class Node:
    # node data structure
    def __init__(self, data, next=None):
        # initialize node with data, link to next_node
        self.data = data
        self.next = next
        
    def set_next(self, next):
        # set link to next node
        self.next = next
        
    def get_next(self):
        # get link to next node
        return self.next
    
    def get_data(self):
        # get data of current node
        return self.data
    
class Stack:
    def __init__(self, limit=1000):
        # initialize stack with default size limit of 1000
        self.top = None # top item of stack
        self.size = 0   # initial size of stack
        self.limit = limit  # size limit of stack
    
    def peek(self):
        # take a look at the top item in stack
        if self.size > 0:
            return self.top.get_data()
        else:
            print("STACK IS EMPTY!")
    
    def push(self, item):
        # push new item onto top of stack
        if self.size < self.limit:  # there is space in stack
            new_item = Node(item)
            new_item.set_next(self.top) 
            self.top = new_item
            self.size += 1  # increment size of stack
        else:
            print("STACK OUT OF SPACE!")
    
    def pop(self):
        # pop top item from the stack
        if self.size > 0:
            remove_item = self.top
            self.top = remove_item.get_next()   # set new top item
            self.size -= 1  # decrement size of stack
            return remove_item.get_data()
        else:
            print("STACK IS EMPTY!")
    
    def print_stack(self):
        # print contents of stack
        top = self.top
        while top:
            print(top.get_data())
            top = top.get_next()    # traverse the stack

# Driver Program
if __name__ == "__main__":
    # demo basic functionality of stack
    s = Stack()
    s.push(1)
    print("pushed 1 to stack")

    print("Top of stack = ", s.peek())

    s.push(2)
    s.push(3)
    s.push(4)
    print("pushed 2, 3 and 4 onto stack")
    print("Top of stack = ", s.peek())

    print("entire stack:")
    s.print_stack()

    print(f"popped {s.pop()} from stack")
    print(f"popped {s.pop()} from stack")
    print("Top of stack = ", s.peek())
    print("entire stack:")
    s.print_stack()