# Class for a binary tree
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    # insert a node
    def insert(self, val):
        """Insert a node into the tree."""
        if val <= self.val:
            if self.left is None:
                self.left = BinaryTreeNode(val)
                print("Inserted", val, "to the left of", self.val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(val)
                print("Inserted", val, "to the right of", self.val)
            else:
                self.right.insert(val)
    
    # in-order traversal
    def in_order_traversal(self):
        """Traverse the tree in-order."""
        if self.left is not None:
            self.left.in_order_traversal()
        print(self.val)
        if self.right is not None:
            self.right.in_order_traversal()
    
    # pre-order traversal
    def pre_order_traversal(self):
        """Traverse the tree pre-order."""
        print(self.val)
        if self.left is not None:
            self.left.pre_order_traversal()
        if self.right is not None:
            self.right.pre_order_traversal()
    
    # post-order traversal
    def post_order_traversal(self):
        """Traverse the tree post-order."""
        if self.left is not None:
            self.left.post_order_traversal()
        if self.right is not None:
            self.right.post_order_traversal()
        print(self.val)

# Test the BinaryTreeNode class
if __name__ == "__main__":
    print("Creating a binary tree... with root node 5")
    root = BinaryTreeNode(5)
    root.insert(3)
    root.insert(7)
    root.insert(2)
    root.insert(4)
    root.insert(6)
    root.insert(8)
    print("In-order traversal:")
    root.in_order_traversal()
    print("Pre-order traversal:")
    root.pre_order_traversal()
    print("Post-order traversal:")
    root.post_order_traversal()