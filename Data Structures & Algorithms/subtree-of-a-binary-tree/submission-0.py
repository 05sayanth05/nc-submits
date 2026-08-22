# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, *args, **kwargs):
        self.__sub_root = None
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if not self.__is_same_tree(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return True


    def __is_same_tree(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        if not root1 and not root2:
            return True
        
        if root1 and root2 and root1.val == root2.val:
            same_ltree = self.__is_same_tree(root1.left, root2.left)
            same_rtree = self.__is_same_tree(root1.right, root2.right)

            return same_ltree and same_rtree
        
        return False


                
        