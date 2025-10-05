class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n = len(board), len(board[0])

        class Node():
            def __init__(self):
                self.children = [None] * 26
                self.bool = False
                self.word = None
        root = Node()
        def insert(string):
            curr = root
            n = len(string)
            for i,x in enumerate(string):

                idx = ord(x) - ord('a')
                if not curr.children[idx]:
                    curr.children[idx] = Node()
                if i == n-1:
                    curr.children[idx].bool =  True
                    curr.children[idx].word = string
                curr = curr.children[idx]
        
        def bfs(f,g,curr):  ##search
            c = board[f][g] 
            idx = ord(board[f][g]) - ord('a')

            if board[f][g] == '#' or not curr.children[idx]:
                return 
            if curr.children[idx].bool:
                ans.append( curr.children[idx].word )
                curr.children[idx].bool = False
                # return

            board[f][g] = '#'
            if f-1 >= 0:
                bfs(f-1,g, curr.children[idx])
            if g-1 >= 0:
                bfs(f,g-1, curr.children[idx])
            if f+1 < m:
                bfs(f+1,g, curr.children[idx])
            if g+1 < n:
                bfs(f,g+1, curr.children[idx])
            
            board[f][g] = c

        
        for w in words:
            insert(w)
        
        ans = []
        for i,x in enumerate(board):
            for j,y in enumerate(x):
                bfs(i,j,root)          #search
        
        return ans