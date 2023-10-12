import unittest
from algo_labs_term3.src.main import BinaryTree


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
