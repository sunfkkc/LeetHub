/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const num = x + ''
    
    return (num === [...num].reverse().join(''))
};