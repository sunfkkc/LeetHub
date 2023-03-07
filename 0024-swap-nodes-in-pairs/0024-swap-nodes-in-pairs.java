/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        
        
        if( head == null || head.next == null){
            
            // base case aka stop condition
            return head;
        }
        
        
        ListNode right = head.next;
        ListNode nextHop = right.next;
        
        // reverse linkage of current pair
        right.next = head;
            
        // reverse next pair and get the node of current head's next node
        head.next = swapPairs( nextHop );
            
        return right;
        
        
    }
}