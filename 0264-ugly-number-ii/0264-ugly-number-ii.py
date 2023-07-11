class Solution(object):
        
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = []
        ans = []
        heapq.heappush(h, 1)
        while len(ans) < n:
            cur = heapq.heappop(h)
            if len(ans) > 0 and ans[-1] == cur:
                continue
            heapq.heappush(h, cur*2)
            heapq.heappush(h, cur*3)
            heapq.heappush(h, cur*5)
            ans.append(cur)

        return ans[n-1]