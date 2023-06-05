# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res=0
        
        def dfs(node):
            
            if not node:
                return
            
            self.res+=1
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return self.res