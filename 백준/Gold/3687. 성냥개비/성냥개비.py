from collections import deque
def cal(n):
    d={0:6,1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6 }
    #max dp
    a={2:1, 3:7}
    #min dp
    b={2:1, 3:7, 4:4, 5:2, 6:6, 7:8, 8:10}
    c={2:1, 3:7, 4:4, 5:2, 6:0, 7:8}

    for i in range(4,n+1):

        a[i] = str(a[i-2]) + str(a[2])
        

    for i in range(9,n+1):
        
        for j in range(2,8):
            if j==2:
                b[i] = b[i-j]*10 + c[j]
                continue
            b[i] = min( b[i],  b[i-j]*10 + c[j] )
    
    print(b[n],a[n])
        
    

n = int(input())
q=deque()
for _ in range(n):
    q.append(int(input()))

while q:
    k=q.popleft()
    cal(k)