# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self._res = 0

        def __height(root: TreeNode | None) -> int:
            if not root:
                return 0

            left_height = __height(root.left)
            right_height = __height(root.right)

            self._res = max(self._res, left_height + right_height)

            return 1 + max(left_height, right_height)

        __height(root)
        return self._res
    
        