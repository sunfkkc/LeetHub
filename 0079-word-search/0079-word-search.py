class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        
        visited=set()
        
        def bt(r,c,i):
            
            if i==len(word):
                return True
            
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or word[i] != board[r][c] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            
            res= bt(r+1,c,i+1) or bt(r-1,c,i+1) or bt(r,c-1,i+1) or bt(r,c+1,i+1)
            
            visited.remove((r,c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if bt(r,c,0):
                    return True
        return False