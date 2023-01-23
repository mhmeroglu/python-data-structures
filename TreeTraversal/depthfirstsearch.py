class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def print_inorder(self):
        result = []
        self.print_inorder_helper(self.root, result)
        return result

    def print_inorder_helper(self, root, result):
        if root is not None:
            self.print_inorder_helper(root.left, result)
            result.append(root.value)
            self.print_inorder_helper(root.right, result)

    def print_preorder(self):
        result = []
        self.print_preorder_helper(self.root, result)
        return result

    def print_preorder_helper(self, root, result):
        if root is not None:
            result.append(root.value)
            self.print_preorder_helper(root.left, result)
            self.print_preorder_helper(root.right, result)

    def print_postorder(self):
        result = []
        self.print_postorder_helper(self.root, result)
        return result

    def print_postorder_helper(self, root, result):
        if root is not None:
            self.print_postorder_helper(root.left, result)
            self.print_postorder_helper(root.right, result)
            result.append(root.value)


my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.print_inorder())
print(my_tree.print_preorder())
print(my_tree.print_postorder())
