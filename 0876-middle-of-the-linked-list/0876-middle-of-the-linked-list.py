# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        fast,slow=head,head
        
        while fast:
            if fast.next:
                slow=slow.next
                fast=fast.next.next
            else:
                break
        return slow