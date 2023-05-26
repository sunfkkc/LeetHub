# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q=deque()
        
        res=[]
        
        q.append(root)
        depth=-1
    
        while q:
            depth+=1
            
            qLen=len(q)
            innerQ=deque()
            for i in range(qLen):
                node = q.popleft()
                
                if node:
                    if depth %2==0:
                        innerQ.append(node.val)
                    else:
                        innerQ.appendleft(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if innerQ:
                res.append(list(innerQ))
        return res