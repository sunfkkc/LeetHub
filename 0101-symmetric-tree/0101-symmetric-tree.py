# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        q = deque()
        q.append((root.left,root.right))
        
        while q:
            
            l,r = q.popleft()
            
            if l and r and l.val == r.val:
                q.append((l.left,r.right))
                q.append((l.right,r.left))
            elif l or r:
                return False
        return True