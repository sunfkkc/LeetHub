/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    
    let answer = 0
    
    if(s.length === 1){return 1}

    for( let i=0; i < s.length-1; i++){
        let substring  = s[i]
        
        for (let j=i+1; j<s.length; j++){
            
            if( s[i] !== s[j] && !substring.includes(s[j])){
                substring += s[j]
                
                
                if(answer < substring.length){
                answer = substring.length
            }
            }
            else{
                if(answer < substring.length){
                answer = substring.length
            }
                break}
            
            
            
        }
    }
    
    return answer
};