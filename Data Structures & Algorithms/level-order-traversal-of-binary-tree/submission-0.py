# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#queue = [1] next_queue = [2,3] level = [] result = []

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        else:
            queue = [root]
            next_queue = []
            level = []
            result = []

            while queue != []:
                for root in queue:
                    level.append(root.val)
                    if root.left is not None:
                        next_queue.append(root.left)
                    if root.right is not None:
                        next_queue.append(root.right)
                result.append(level)
                level = []
                queue = next_queue
                next_queue = []
        
        return result
                



        