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
    public ListNode mergeKLists(ListNode[] lists) {
        
        
        
        
        int k = lists.length;
        
        ListNode answer = new ListNode();
        
        ListNode cur = answer;
        

        
        
        outer : while(true){
            boolean allNull = true;
            
            int index=0;
            int min = 10001;
            
            for( int i = k-1; i>=0; i--){
                
                if( lists[i] != null){
                    
                    allNull = false;
                        
                    
                    if( lists[i].val < min){
                        
                        index = i;
                        min = lists[i].val;
                    }
                    
                    
                }
                
                
                
            }
            
            if(allNull) break outer;
            
            
            
            
            cur.next = lists[index];
            lists[index] = lists[index].next;
            
            
            cur = cur.next;

            
            
        }
        
        
        
        return answer.next;
        
    }
}

