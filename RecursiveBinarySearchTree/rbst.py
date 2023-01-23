class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_inorder(self):
        result = []
        self.print_inorder_helper(self.root, result)
        return result

    def print_inorder_helper(self, root, result):
        if root is not None:
            self.print_inorder_helper(root.left, result)
            result.append(root.value)
            self.print_inorder_helper(root.right, result)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.insert_helper(self.root, value)

    def insert_helper(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self.insert_helper(root.left, value)
        if value > root.value:
            root.right = self.insert_helper(root.right, value)
        return root

    def contains(self, value):
        return self.contains_helper(self.root, value)

    def contains_helper(self, root, value):
        if root is None:
            return False
        if value == root.value:
            return True
        if value < root.value:
            return self.contains_helper(root.left, value)
        if value > root.value:
            return self.contains_helper(root.right, value)

    def min_value(self, root):
        if root is None:
            return
        if root.left is None:
            return root.value
        return self.min_value(root.left)

    def delete(self, value):
        self.delete_helper(self.root, value)

    def delete_helper(self, root, value):
        if root is None:
            return None
        if value < root.value:
            root.left = self.delete_helper(root.left, value)
        elif value > root.value:
            root.right = self.delete_helper(root.right, value)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                sub_tree_min = self.min_value(root.right)
                root.value = sub_tree_min
                root.right = self.delete_helper(root.right, sub_tree_min)
        return root

