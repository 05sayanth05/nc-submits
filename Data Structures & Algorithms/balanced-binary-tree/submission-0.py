# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        l_height = 1 + self.dfs(root.left)
        r_height = 1 + self.dfs(root.right)

        self.__is_balanced = self.__is_balanced and abs(l_height - r_height) < 2

        return max(l_height, r_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.__is_balanced = True

        self.dfs(root)

        return self.__is_balanced