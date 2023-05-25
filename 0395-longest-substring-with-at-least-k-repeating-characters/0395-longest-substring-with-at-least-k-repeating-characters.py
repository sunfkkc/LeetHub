class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 0
        for T in range(1, len(Counter(s)) + 1):
            beg = 0
            end = 0
            Found = 0
            MoreEqK = 0
            freq = [0]*26
            while end < len(s):
                if MoreEqK <= T:
                    idx = ord(s[end]) - ord('a')
                    freq[idx] += 1
                    if freq[idx] == 1:
                        MoreEqK += 1
                    if freq[idx] == k:
                        Found += 1
                    end += 1
                else:
                    idx = ord(s[beg]) - ord('a')
                    if freq[idx] == k:
                        Found -= 1
                    freq[idx] -= 1
                    if freq[idx] == 0:
                        MoreEqK -= 1
                    beg += 1

                if MoreEqK == Found:
                    result = max(result, end - beg)
        return result