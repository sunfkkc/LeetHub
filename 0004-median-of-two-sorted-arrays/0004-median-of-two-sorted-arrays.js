/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    const merged = nums1.concat(nums2).sort((a,b)=>a-b)
    console.log(merged)
    const midpoint = Math.floor(merged.length / 2);
    
    const median = merged.length % 2 === 1 ?
    merged[midpoint] : 
    (merged[midpoint - 1] + merged[midpoint]) / 2;
    
  return median;
};