class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        self.res=0
        
        def cal(men):
            
            s=0
            for i in range(len(students)):
                for j in range(len(students[0])):
                    
                    s+=1 if students[i][j]==men[i][j] else 0
            return s
        
        
        def bt(i,temp,v):
            
            if i==len(mentors):
                self.res=max(self.res,cal(temp))
                return
            
            for m in range(len(mentors)):
                
                if m not in v:
                    v.add(m)
                    bt(i+1,temp+[mentors[m]],v)
                    v.remove(m)
                    
        v=set()
        
        bt(0,[],v)
        
        return self.res