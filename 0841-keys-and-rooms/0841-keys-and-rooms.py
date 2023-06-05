class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        visited=[0]
        
        
        stack=[rooms[0]]
        
        
        while stack:
            
            keys=stack.pop()
            for key in keys:
                
                if key not in visited:
                    
                    visited.append(key)
                    stack.append(rooms[key])
                    
        return True if len(visited)==len(rooms) else False
        