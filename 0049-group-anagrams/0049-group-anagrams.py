class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        
        d=defaultdict(list)
        
        for s in strs:
            d[str(sorted(s))].append(s)
            
        return [i for i in d.values()]