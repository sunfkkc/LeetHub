class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        hs=[0]*numCourses
        course_map=defaultdict(list)
        
        for after,pre in prerequisites:
            hs[after] +=1
            course_map[pre].append(after)
        
        
        rst=[i for i in range(len(hs)) if hs[i]==0]
        q=deque(rst)
        
        while q:
            course = q.popleft()
            
            for c in course_map[course]:
                hs[c]-=1
                if hs[c]==0:
                    rst.append(c)
                    q.append(c)
        if not any(hs):
            return rst
        return []