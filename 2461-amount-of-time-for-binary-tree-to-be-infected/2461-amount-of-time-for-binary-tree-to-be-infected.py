# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        #lets convert the tree into the graph
        self.adj_list = collections.defaultdict(list)
        def create_graph(node):
            if not node:
                return
            if node.left:
                self.adj_list[node.val].append(node.left.val)
                self.adj_list[node.left.val].append(node.val)
            if node.right:
                self.adj_list[node.val].append(node.right.val)
                self.adj_list[node.right.val].append(node.val)
            create_graph(node.left)
            create_graph(node.right)
        

        create_graph(root)

        q = deque([(start,0)])
        visit = set()
        res = 0
        print(self.adj_list)
        while q:
            node,time = q.popleft()
            res = max(res,time)
            visit.add(node)
            for j in self.adj_list[node]:
                if j not in visit:
                    q.append((j,time+1))
            
        return res



            


