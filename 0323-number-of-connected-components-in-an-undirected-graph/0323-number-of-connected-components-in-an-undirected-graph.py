class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        res = n
        #union find method
        def find(n1):
            x = n1
            while x!=parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2
            
            return 1


        for n1,n2 in edges:
            res -=union(n1,n2)

        return res