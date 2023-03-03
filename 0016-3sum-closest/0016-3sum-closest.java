class Solution {
    
    
    
    public int threeSumClosest(int[] nums, int target) {
        
        Arrays.sort(nums);
        
        int answer = nums[0] + nums[1] + nums[nums.length-1];
        int dif = Math.abs( answer - target);
        
        
        
        
        outer : for( int i=0; i< nums.length-2; i++){
            
            int j = i + 1;
            int k = nums.length-1;
            
            while( j < k){
                
                int sum = nums[i] + nums[j] + nums[k];
                
                
                    
                if( sum >= target){
                    
                    if( Math.abs(sum-target) < dif ){
                        answer = sum;
                        dif = Math.abs(sum-target);
                    }
                    k--;
                    
                }
                else{
                    
                    if( Math.abs(sum-target) < dif ){
                        answer = sum;
                        dif = Math.abs(sum-target);
                    }
                    
                    j++;
                }
            }
        }
        
        return answer;
        
        
    }
}