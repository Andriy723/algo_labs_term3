class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def height(self, node):
        if node is None:
            return 0

        height_left = self.height(node.left)
        height_right = self.height(node.right)

        if abs(height_left - height_right) > 1 or height_right == -1 or height_left == -1:
            return -1
        return max(height_left, height_right) + 1

    def is_tree_balanced(self, node) -> bool:
        if node is None:
            return True

        height_left = self.height(node.left)
        height_right = self.height(node.right)

        if max(height_left, height_right) - min(height_left, height_right) > 1 \
                or height_left == -1 or height_right == -1:
            return False
        else:
            return True
