def solution(n, results):
    answer = 0
    
    dist = [ [0]*n for i in range(n)]
    
    for a,b in results:
        dist[a-1][b-1]=1
        dist[b-1][a-1]=-1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                
                if dist[i][j]==0 and i != j and j != k:
                    
                    if dist[i][k] + dist[k][j] ==2:
                        dist[i][j]=1
                    if dist[i][k] + dist[k][j] ==-2:
                        dist[i][j]=-1
    for i in range(n):
        c=0
        for j in range(n):
            if dist[j][i]==0:
                c+=1
        
        if c ==1:
            answer+=1
    
    return answer