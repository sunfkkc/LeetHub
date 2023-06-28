class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        i=0
            
        
        while i <len(flowerbed):
            if n==0:
                break
            
            if flowerbed[i]==0:
                if flowerbed[max(i-1,0)]==0 and flowerbed[min(i+1,len(flowerbed)-1)]==0:
                    n-=1
                        
                    i+=2
                    continue
                i+=1
                
            else:
                i+=1
                
                
        return True if n==0 else False