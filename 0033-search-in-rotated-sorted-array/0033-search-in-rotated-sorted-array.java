class Solution {
    public int search(int[] nums, int target) {
        
        return IntStream.range(0, nums.length)
                    .filter(i -> target == nums[i])
                    .findFirst()
                    .orElse(-1);    // 타겟을 찾지 못하면 -1 반환
    }
}