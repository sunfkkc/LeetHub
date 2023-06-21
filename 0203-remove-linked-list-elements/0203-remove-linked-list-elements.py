# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dum=ListNode(next=head)
        cur,prev=head,dum
        
        while cur:
            nxt=cur.next
            if cur.val ==val:
                prev.next=nxt
            else:
                prev=cur
            cur=nxt
        return dum.next