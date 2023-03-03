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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        if( head.next == null) return null; //원소가 1개일 경우 무조건 null
        
        ListNode a = head;
        
        ListNode b = head;
        
        while( n > 0){
            b = b.next;
            n--;
        }
        
        if(b == null) {
            
            return head.next;
        } // n이 head의 노드의 개수와 같을때 
        
        
        
        while( b.next != null){
            b = b.next;
            a = a.next;
        }
        

        
        a.next = a.next.next;
        

        return head;
        
    }
}