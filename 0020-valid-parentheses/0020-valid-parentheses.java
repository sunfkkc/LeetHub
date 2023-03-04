class Solution {
    public boolean isValid(String s) {
        
        if( s.length() == 1) return false;
        
        if( s.charAt(0) == 41 || s.charAt(0) == 93 || s.charAt(0) == 125) return false;
        
        StringBuilder MyString = new StringBuilder(s);
        
        int i=1;
        
        while (MyString.length() != 0){
            
            if( i == 0){
                if( MyString.charAt(i) == 41 || MyString.charAt(i) == 93 || MyString.charAt(i) == 125) return false;
                i++;
            }
            
            if( i == MyString.length()) return false;
            
            if( MyString.charAt(i) == 41 || MyString.charAt(i) == 93 || MyString.charAt(i) == 125){
                
                if( Math.abs(MyString.charAt(i) - MyString.charAt(i-1) ) >2 ){
                    

                    return false;
                }
                
                
                MyString.deleteCharAt(i);
                MyString.deleteCharAt(i-1);
                
                
                i--;
                
            }
            
            
            else{
                i++;
                
            }
            
            
        }
        

        
        return true;        
    }
}