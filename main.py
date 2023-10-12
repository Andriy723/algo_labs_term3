import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def height(self, node):
        if node is None:
            return 1

        height_left = self.height(node.left)
        height_right = self.height(node.right)

        return max(height_left, height_right) + 1

    def is_tree_balanced(self, node) -> bool:
        if node is None:
            return True

        height_left = self.height(node.left)
        height_right = self.height(node.right)

        a = max(height_left, height_right)
        b = min(height_left, height_right)
        c = a - b

        if c > 1:
            return False
        else:
            return True

class Test(unittest.TestCase):
    def test_equal_1(self):

        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)

        self.assertTrue(root.is_tree_balanced(root))

    def test_equal_2(self):

        root = BinaryTree(1)
        root.left = BinaryTree(12)
        root.right = BinaryTree(25)
        root.left.left = BinaryTree(10)
        root.left.left.left = BinaryTree(5)

        self.assertFalse(root.is_tree_balanced(root))

    def test_equal_3(self):

        root = BinaryTree(111)
        root.left = BinaryTree(121)
        root.right = BinaryTree(156)
        root.right.right = BinaryTree(200)
        root.right.right.right = BinaryTree(250)

        self.assertFalse(root.is_tree_balanced(root))
