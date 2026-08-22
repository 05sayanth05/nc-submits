# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TraverseNode:
    def __init__(self, node: TreeNode, level: int):
        self.node = node
        self.level = level


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        print(root)
        
        queue: list[TraverseNode] = [TraverseNode(root, 0)]

        levels: list[list[int]] = []

        while len(queue) > 0:
            elem = queue.pop(0)
            
            node = elem.node
            
            level = elem.level
            next_level = level + 1

            print(node.val, end=" ")
            if len(levels) - 1 < level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                queue.append(TraverseNode(node.left, next_level))
            
            if node.right:
                queue.append(TraverseNode(node.right, next_level))
        
        return levels
