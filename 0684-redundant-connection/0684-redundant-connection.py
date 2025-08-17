class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1] * (len(edges)+1)
        parent = [i for i in range(len(edges)+1)]
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
                return True
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2
            return False
        
        for n1,n2 in edges:
            if union(n1,n2):
                return [n1,n2]
        return []
