class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        visited=set()
        
        
        
        stack=[]
        stack.append((sr,sc))
        
        origin=image[sr][sc]
        
        while stack:
            
            r,c=stack.pop()
                
            if r<0 or r>=len(image) or c<0 or c>=len(image[0]):
                continue
            
            if image[r][c] == origin:
                
                image[r][c]=color
            
                if (r,c) not in visited:
                    visited.add((r,c))
                    stack.append((r-1,c))
                    stack.append((r+1,c))
                    stack.append((r,c-1))
                    stack.append((r,c+1))
                
        
        return image