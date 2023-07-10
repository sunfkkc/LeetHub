class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a=[-i for i in nums]
        heapq.heapify(a)
        for i in range(k):
            res=heapq.heappop(a)
        return -res