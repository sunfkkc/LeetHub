"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        q=deque()
        
        q.append(root)
        
        while q:
            qLen = len(q)
            
            for i in range(qLen):
                
                node = q.popleft()
                
                if node:
                    
                    if i != qLen-1:
                        node.next=q[0]
                    
                    
                    if node.left:
                        q.append(node.left)
                        q.append(node.right)
        return root