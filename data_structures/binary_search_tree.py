# Description: This file contains the class definition for a binary search tree node.
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    # insert a node into the tree
    def insert(self, val):
        """Insert a node into the tree."""
        if val <= self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
    
    # find a node in the tree
    def find(self, val):
        """Find a node in the tree."""
        if val < self.val:
            if self.left is None:
                return False
            else:
                return self.left.find(val)
        elif val > self.val:
            if self.right is None:
                return False
            else:
                return self.right.find(val)
        else:
            return True
            
    # in-order traversal
    def in_order_traversal(self):
        """Traverse the tree in-order."""
        if self.left is not None:
            self.left.in_order_traversal()
        print(self.val)
        if self.right is not None:
            self.right.in_order_traversal()
    
    # delete a node from the tree
    def delete(self, val):
        """Delete a node from the tree."""
        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                self.val = self.right.find_min_value()
                self.right = self.right.delete(self.val)
        return self
    
    def find_min_value(self):
        """Find the minimum value in the tree."""
        if self.left is None:
            return self.val
        return self.left.find_min_value()
    
# Test the BSTNode class
if __name__ == '__main__':
    root = BSTNode(10)
    root.insert(5)
    root.insert(15)
    root.insert(8)
    root.insert(3)
    root.insert(12)
    root.insert(20)
    root.insert(13)
    root.insert(14)
    root.insert(17)
    root.insert(25)
    root.in_order_traversal()
    print(root.find(17))
    print(root.find(100))
    root.delete(15)
    root.in_order_traversal()