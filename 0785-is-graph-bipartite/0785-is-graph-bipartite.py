class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """  
        visited=set()
        
        
        def search(i):
            if not graph[i]:
                return True
            
            if i in visited:
                return True
            
            a=set()
            b=set()
            
            q=deque([i])
            
            visited.add(i)
            toggle=True
            while q:

                for j in range(len(q)):

                    n=q.popleft()

                    visited.add(n)

                    if toggle:

                        a.add(n)
                    else:
                        b.add(n)

                    for i in graph[n]:

                        if toggle:
                            if i in a:
                                return False
                        else:
                            if i in b:
                                return False


                        if i not in visited:
                            q.append(i)
                            visited.add(i)



                toggle = not toggle

            return True
        
        for i in range(len(graph)):
            if not search(i):
                return False
        return True
        