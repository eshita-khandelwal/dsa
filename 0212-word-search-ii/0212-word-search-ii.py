class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addChildren(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addChildren(word)
        row = len(board)
        col = len(board[0])
        res,visit = set(),set()


        def dfs(r,c,word,node):
            if (r,c) in visit or r<0 or c<0 or c==col or r==row or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r,c+1,word,node)
            dfs(r+1,c,word,node)
            dfs(r,c-1,word,node)
            dfs(r-1,c,word,node)
            visit.remove((r,c))

        for r in range(row):
            for c in range(col):
                dfs(r,c,"",root)
        
        return list(res)
            
        