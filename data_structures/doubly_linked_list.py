class Node:
  # node data structure
    def __init__(self, data, next=None, prev=None):
        # initialize node with data, link to next_node
        self.data = data
        self.next = next
        self.prev = prev
    
    def set_next(self, next):
        # set link to next node
        self.next = next
    
    def get_next(self):
        # get link to next node
        return self.next
  
    def set_prev(self, prev):
        # set link to previous node
        self.prev = prev
    
    def get_prev(self):
        # get link to previous node
        return self.prev
  
    def get_data(self):
        # get data of current node
        return self.data

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_head(self, data):
        # add new head to doubly linked list
        new_head = Node(data)   # create new head
        current_head = self.head    # get current head
        if current_head != None:
            current_head.set_prev(new_head) # link prev link of current node to new node
            new_head.set_next(current_head) # link next node of new node to current node

        self.head = new_head    # add new head
        if self.tail == None:   # if tail does not exist, make tail same as head
            self.tail = new_head

    def add_tail(self, data):
        # add new tail to doubly linked list
        new_tail = Node(data)   # create new tail
        current_tail = self.tail    # get current tail
        if current_tail != None:
            current_tail.set_next(new_tail) # link next link of current tail to new tail
            new_tail.set_prev(current_tail) # link prev link of new tail to current tail
        
        self.tail = new_tail    # add new tail
        if self.head == None:   # if head does not exist, make head same as tail
            self.head = new_tail

    def remove_head(self):
        # remove head from doubly linked list
        removed_head = self.head
        if removed_head == None:    # head node does not exist
            return None
        
        self.head = removed_head.get_next() # set head to removed head's next node
        if self.head != None:
            self.head.set_prev(None)    # unlink prev node of new head

        if removed_head == self.tail:   # if removed head is same as tail, call remove tail
            self.remove_tail()
        
        return removed_head.get_data()  # return data of removed head

    def remove_tail(self):
        # remove tail from doubly linked list
        removed_tail = self.tail
        if removed_tail == None:    # tail node does not exist
            return None
        
        self.tail = removed_tail.get_prev() # set tail to removed tail's prev node
        if self.tail != None:
            self.tail.set_next(None)    # unlink next node of new tail
        
        if removed_tail == self.head:   # if removed tail is same as head, call remove head
            self.remove_head()

        return removed_tail.get_data()  # return data of removed tail

    def remove_data(self, data):
        # remove node by data
        remove_node = None  # node to be removed

        current_node = self.head
        while current_node != None: # traverse node from head to tail
            if current_node.get_data() == data:
                remove_node = current_node  # found node to be removed
                break
            current_node = current_node.get_next()  # go to next node
        
        if remove_node == None: # node to be removed by data does not exist
            return None
        
        if remove_node == self.head:    # if node to remove is head, then call remove_head
            self.remove_head()
        elif remove_node == self.tail:  # if node to remove is tail, then call remove_tail
            self.remove_tail()
        else:
            next = remove_node.get_next()   # node to be removed's next node
            prev = remove_node.get_prev()   # node to be removed's prev node
            next.set_prev(prev) # link prev node of next to prev
            prev.set_next(next) # link next node of prev to next
        return remove_node
    
    def print_dllist(self):
        # print all nodes within doubly linked list
        current_node = self.head
        while current_node:
            if current_node.get_next() == None:
                print(current_node.get_data())  # print node without '<->'
            else:
                print(current_node.get_data(), end = '<->') # print nodes with '<->'
            current_node = current_node.get_next()  # go to next node


# Driver Program
if __name__ == "__main__":
  # demo basic functionality of double linked list
  dll = DoubleLinkedList()    # initialize new double linked list
  print("created new double linked list")

  dll.add_head(3)
  print("added new head 3")
  dll.add_tail(4)
  print("added new tail 4")
  dll.print_dllist()

  dll.add_tail(5)
  print("added 5 to tail")
  dll.print_dllist()
  dll.add_head(2)
  print("added 2 to head")
  dll.print_dllist()
  dll.add_head(1)
  print("added 1 to head")
  dll.print_dllist()

  dll.remove_head()
  print("removed head")
  dll.print_dllist()

  dll.remove_tail()
  print("removed tail")
  dll.print_dllist()

  dll.remove_data(3)
  print("remove by data: 3")
  dll.print_dllist()


