# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        q=deque([root])
        
        while q:
            
            n = q.popleft()
            
            if n.val==val:
                return n
            
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
                
        return None