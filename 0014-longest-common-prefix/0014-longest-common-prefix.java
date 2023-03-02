class Solution {
    public String longestCommonPrefix(String[] strs) {
        String answer = "";
        
        Outer : for( int i=0; i< strs[0].length(); i++){
            for( String s : strs){
                
                try{
                if( s.charAt(i) != strs[0].charAt(i)){
                    break Outer;
                }
                } catch(Exception e){
                    break Outer;
                }
            }
            
            answer += strs[0].charAt(i);
        }
        
        return answer;
    }
}