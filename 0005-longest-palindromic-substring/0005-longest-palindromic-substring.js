/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    
    if(s.length === 1){
        return s
    }
    
    let answer = ''
    
    for( let i=0; i<s.length-1; i++){
        
        let substring = s[i]
        
        for( let j=i+1; j< s.length; j++){
            
            substring += s[j]

            if(s[i] !== s[j]) continue

            
            if( substring.length > answer.length && isPalindromic(substring) ){
                answer = substring
                console.log(answer)
            }
        }
        
        
    }
    
    return answer=== "" ? s[0] : answer
};


const isPalindromic = (string) => {
    return string === [...string].reverse().join('');
}