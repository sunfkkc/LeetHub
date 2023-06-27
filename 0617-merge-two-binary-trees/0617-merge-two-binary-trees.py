# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        if not root2:
            return root1
        
        q=deque()
        
        q.append([root1,root2])
        
        while q:
            n1,n2=q.popleft()
            
            
            
            n=(n1.val or 0) + (n2.val or 0)
            n1.val=n
            

                
            if n1.left and n2.left:
                q.append([n1.left,n2.left])
            
            if n1.right and n2.right:
                q.append([n1.right,n2.right])
                
            if not n1.left:
                n1.left=n2.left
                
            if not n1.right:
                n1.right=n2.right
        return root1
                