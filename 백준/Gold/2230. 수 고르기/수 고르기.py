n,m = map(int,input().split())

a=[]

for i in range(n):
    k=int(input())
    a.append(k)

a.sort()

l,r=0,0
res=float('inf')
while l<=r and l <n and r<n:

    if a[r]-a[l] >=m:
        res=min(res,a[r]-a[l])
        l+=1
    else:
        r+=1

print(res)