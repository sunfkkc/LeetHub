class Solution:
    def canPartitionKSubsets(self, nums, k):
        n = len(nums)

        if sum(nums)%k != 0: return False

        target = sum(nums)//k

        nums.sort(reverse = True)

        def backtrack(i,ans):
            if i == n:
                return len(set(ans)) == 1

            for j in range(k):
                if ans[j] + nums[i] <= target:
                    ans[j] += nums[i]

                    if backtrack(i+1,ans):
                        return True

                    ans[j] -= nums[i]

                    if not ans[j]: break

            return False

        return backtrack(0,[0]*k)