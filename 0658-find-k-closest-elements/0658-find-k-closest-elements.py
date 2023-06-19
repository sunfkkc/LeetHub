class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        if x<=arr[0] : return arr[:k]
        if arr[-1]<=x : return arr[-k:]
        l=0
        r=len(arr)-1
        
        while l<r:
            
            mid=(l+r)//2
            
            if arr[mid]<=x<arr[mid+1]:
                break
            elif x<arr[mid]:
                r=mid
            else:
                l=mid
                
        def cal(a,b,x):
            if b==len(arr): return True
            return abs(arr[a]-x)<=abs(arr[b]-x)
        
        c=0
        a=mid
        b=mid+1
        while c<k:
            if cal(a,b,x):
                a-=1
            else:
                b+=1
            c+=1
            
        return [arr[i] for i in range(a+1,b)]