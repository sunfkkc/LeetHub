# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=0
        
        stack=[(root,root.val)]
        
        while stack:
            
            node, num=stack.pop()
            
            if not node.left and not node.right:
                res+=num
                continue
            
            
            if node.left:
                
                stack.append((node.left, int( str(num)+str(node.left.val) ) ))
                
            if node.right:
                
                stack.append((node.right, int( str(num) + str(node.right.val) )))
        return res