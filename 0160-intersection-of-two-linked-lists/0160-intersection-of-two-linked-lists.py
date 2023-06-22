# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        cA,cB = 0,0
        
        pA,pB = headA,headB
        
        while pA:
            pA = pA.next
            cA+=1
            
        while pB:
            pB=pB.next
            cB+=1
        pA,pB = headA,headB
        if cA>cB:
            while cA != cB:
                pA=pA.next
                cA-=1
        else:
            while cB != cA:
                pB=pB.next
                cB-=1
        
        while pA != pB:
            pA=pA.next
            pB=pB.next
        return pA