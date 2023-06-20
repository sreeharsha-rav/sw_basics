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

class LinkedList:
  # Linked List data structure
  def __init__(self, data=None):
    # initialize linked list with head node
    self.head = Node(data)

  def get_head(self):
    # get current head node
    return self.head
  
  def insert_first(self, new_data):
    # insert new_data at the beginning of linked list
    new_node = Node(new_data) # create new node
    new_node.set_next(self.head)  # link new node to current head node
    self.head = new_node  # change head to new node
  
  def insert_end(self, new_data):
    # insert new_data at the end of linked list
    new_node = Node(new_data) # create new node
    current_node = self.head
    
    if current_node == None:  # if linked list is empty, make head as new_data
      self.head = new_node
      return
    
    while current_node: # traverse node from head to end
      if current_node.get_next() == None: # set last node link to new node
        current_node.set_next(new_node)
        return
      current_node = current_node.get_next()  # move to next node
  
  def insert_after(self, prev_data, new_data):
    # insert new_data after prev_node in linked list
    if self.head == None:
      print("Linked List is empty")
      return
    
    new_node = Node(new_data) # create new node
    current_node = self.head

    while current_node: # traverse node from head to end
      if current_node.get_data() == prev_data:
        new_node.set_next(current_node.get_next())  # link new_node to the node after prev_data node
        current_node.set_next(new_node) # link prev_data node to new_node
        return
      current_node = current_node.get_next()  # move to next node
    
    print("Node with", prev_data, "data not found")

  def remove_node(self, del_data):
    # deletes del_data from linked list
    current_node = self.head  # start from head node

    if current_node == None:
      print("Linked List is empty")
      return
    
    if current_node.get_data() == del_data:  # if first node is the one to be deleted
      next_node = current_node.get_next()
      current_node = next_node  # change head to next node
      return
    
    prev_node = current_node # set first node as previous node
    next_node = current_node.get_next()  # set second node as next node

    while next_node:
      if next_node.get_data() == del_data:
        prev_node.set_next(next_node.get_next()) # link previous node to next node's next link/node, skipping the node containing del_data
        return
      prev_node = next_node # move prev node to current next_node
      next_node = next_node.get_next()  # move next node to next link

    print("Node with", del_data, "data not found")

  def has_node(self, node):
    # to check whether node exists within linked list or not
    current_node = self.head
    while current_node:
      if current_node == node:
        return True
      current_node = current_node.get_next()  # move to next node
      
    return False

  def print_llist(self):
    # print all nodes with link in the linked list
    current_node = self.head
    while current_node: # traverse node from head to end
      if current_node.get_next() == None:
        print(current_node.get_data())  # print last node without '->'
      else:
        print(current_node.get_data(), end = " -> ") # print nodes with '->'
      current_node = current_node.get_next()  # go to next node


# Driver Program
if __name__ == "__main__":
  # demo basic functionality of linked list  
  ll_1 = LinkedList(3)  # create new linked list with 3 as head node
  print("created new linked list")
  ll_1.print_llist()

  ll_1.insert_first(2)
  print("inserted 2 at beginning")
  ll_1.print_llist()

  ll_1.insert_first(1)
  print("inserted 1 at beginning")
  ll_1.print_llist()

  ll_1.insert_end(5)
  print("inserted 5 at end")
  ll_1.print_llist()

  ll_1.insert_after(3,4)
  print("inserted 4 after 3")
  ll_1.print_llist()
  
  ll_1.remove_node(1)
  print("removed 1 from linked list")
  ll_1.print_llist()

  print("is 3 present in linked list? ", ll_1.has_node(3))

  ll_1.remove_node(3)
  print("removed 3 from linked list")
  ll_1.print_llist()

  print("is 3 present in linked list? ", ll_1.has_node(3))

  ll_1.remove_node(5)
  print("removed 5 from linked list")
  ll_1.print_llist()