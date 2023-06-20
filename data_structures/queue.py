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
    
class Queue:
    def __init__(self):
        # initialize queue with default unlimited size
        self.head = None    # first node at front of queue
        self.tail = None    # last node at back of queue
        self.size = 0   # initial size of queue
    
    def peek(self):
        # get node at the front of queue
        if self.size > 0:
            return self.head.get_data()
        else:
            print("QUEUE IS EMPTY!")
    
    def enqueue(self, item):
        # add a node to the back of queue
        if True:
            new_item = Node(item)
            if self.size == 0:
                self.head = new_item    # make new item as the new head and new tail
                self.tail = new_item
            else:
                self.tail.set_next(new_item)    # link current tail to new item
                self.tail = new_item    # make new item as the tail
            self.size += 1

    def dequeue(self):
        # remove a node from the front of queue
        if self.size > 0:
            remove_item = self.head # item to be removed at front of queue
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = remove_item.get_next()  # set next item as new head
            self.size -= 1  # decrement queue size
            return remove_item.get_data()
        else:
            print("QUEUE IS EMPTY!")

    def print_queue(self):
        # print contents of queue
        front = self.head
        while front:
            if(front.get_next() == None):
                print(front.get_data())
            else:
                print(front.get_data(), end = '<-')
            front = front.get_next()    # traverse the queue
        

# Driver Program
if __name__ == "__main__":
    # demo basic functionality of queue
    q = Queue()
    print("created a queue")
    print("enqueue 1")
    q.enqueue(1)
    print("Front of queue = ", q.peek())

    print("enqueue 2, 3, 4")
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print("Contents of queue:")
    q.print_queue()

    print(f"dequeued {q.dequeue()}")
    print("Contents of queue:")
    q.print_queue()

    print(f"dequeued {q.dequeue()}")
    print(f"dequeued {q.dequeue()}")
    print("Contents of queue:")
    q.print_queue()