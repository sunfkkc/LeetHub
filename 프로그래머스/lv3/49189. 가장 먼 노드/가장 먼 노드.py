from collections import defaultdict,deque
def solution(n, edge):
    
    adj=defaultdict(set)
    dist=[float('inf') for i in range(n+1)]
    dist[1]=0
    
    for a,b in edge:
        adj[a].add(b)
        adj[b].add(a)
    
    q = deque()
    
    for i in list(adj[1]):
        q.append((i,1))
        
    while q:
        v,c=q.popleft()
        
        if dist[v] <= c:
            continue
        
        dist[v]=c
        
        for i in list(adj[v]):
            
            if dist[i] > c+1 :
                q.append((i,c+1))
    
    
    m = max(dist[1:])
    
    return dist[1:].count(m)