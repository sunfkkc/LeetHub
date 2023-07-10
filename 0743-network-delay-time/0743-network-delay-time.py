class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj=defaultdict(list)

        for i in times:
            adj[i[0]].append([i[1],i[2]])

        dist = [float('inf')]*(n+1)
        dist[k]=0
        heap=[]

        heapq.heappush(heap,[0,k])

        while heap:

            cost,node = heapq.heappop(heap)

            for no,co in adj[node]:
                co+=cost

                if co<dist[no]:
                    dist[no]=co
                    heapq.heappush(heap,[co,no])
                    
        return -1 if max(dist[1:])==float('inf') else max(dist[1:])

