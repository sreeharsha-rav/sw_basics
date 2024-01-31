class TreeNode:
    """A class representing a node in a tree."""
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child_node):
        """Add a child node to self.children."""
        self.children.append(child_node)

    def remove_child(self, child_node):
        """Remove a child node from self.children."""
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self):
        """Traverse the tree."""
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.val)
            nodes_to_visit += current_node.children

# Test the TreeNode class
if __name__ == "__main__":
    root = TreeNode("CEO")
    first_child = TreeNode("Vice-President")
    second_child = TreeNode("Head of Marketing")
    third_child = TreeNode("Marketing Assistant")
    fourth_child = TreeNode("Head of Engineering")
    fifth_child = TreeNode("Software Engineer")
    sixth_child = TreeNode("Software Engineer")
    seventh_child = TreeNode("Head of Sales")
    eighth_child = TreeNode("Sales Representative")
    ninth_child = TreeNode("Sales Representative")
    root.add_child(first_child)
    root.add_child(second_child)
    second_child.add_child(third_child)
    root.add_child(fourth_child)
    fourth_child.add_child(fifth_child)
    fourth_child.add_child(sixth_child)
    root.add_child(seventh_child)
    seventh_child.add_child(eighth_child)
    seventh_child.add_child(ninth_child)
    root.traverse()