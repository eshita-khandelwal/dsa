class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        res = n
        rank = [1] * n
        parent = [i for i in range(n)]
        def find(n1):
            x = n1
            while x!=parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2
            return True
        
        for n1,n2 in edges:
            if union(n1,n2):
                res -=1
            else:
                return False
        return res == 1
            