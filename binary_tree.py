class Tree:

    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        return True

    def _search(self, node_to_check, value):
        if (node_to_check is None) or (node_to_check.value == value):
            return node_to_check

        if value > node_to_check.value:
            # go right
            return self._search(node_to_check.right, value)
        else:
            # go left
            return self._search(node_to_check.left, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value > current_node.value:
            # add to the right
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
            self._insert(current_node.right, value)
        else:
            # add to the left
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            self._insert(current_node.left, value)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, current_node):
        print(current_node.value)
        if current_node.left is not None:
            self._print_tree(current_node.left)
        if current_node.right is not None:
            self._print_tree(current_node.right)

    def max_value(self):
        pass

    def min_value(self):
        pass

    def delete(self):
        pass


class Node:
    def __init__(self, value, parent=None):
        self.right = None
        self.left = None
        self.parent = parent
        self.value = value


tree = Tree()
tree.insert(10)
tree.insert(8)
tree.insert(6)
print(tree.search(10))
print(tree.search(8))
print(tree.search(6))
tree.print_tree()
