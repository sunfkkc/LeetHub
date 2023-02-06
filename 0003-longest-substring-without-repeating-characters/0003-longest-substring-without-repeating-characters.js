/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    
    let answer = 0
    
    if(s.length === 1){return 1}

    for( let i=0; i < s.length-1; i++){
        let substring  = s[i]
       // console.log(s[i],'====start====')
        
        for (let j=i+1; j<s.length; j++){
           // console.log(s[j],'sub start')
            
            if( s[i] !== s[j] && !substring.includes(s[j])){
                substring += s[j]
                
                //console.log('different',substring)
                
                if(answer < substring.length){
                answer = substring.length
                //console.log('change answer',substring.length)
                //console.log('substring',substring)
            }
            }
            else{
                if(answer < substring.length){
                answer = substring.length
                //console.log('change answer',substring.length)
                //console.log('substring',substring)
            }
                break}
            
            
            
        }
    }
    
    return answer
};