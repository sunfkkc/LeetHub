n,s = map(int,input().split())

a = list(map(int,input().split()))

l,r=0,0
res=float('inf')
b=a[0]
while True:

    if b<s:
        r+=1
        if r==n: break
        b+=a[r]
    else:
        res=min(res,r-l+1)
        b-=a[l]
        l+=1

print( 0 if res==float('inf') else res)
        