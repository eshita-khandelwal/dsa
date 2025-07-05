# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #convert to a graph:
        adj_list = collections.defaultdict(list)
        def graph_convert(node):
            if not node:
                return
            if node.left:
                adj_list[node.left.val].append(node.val)
                adj_list[node.val].append(node.left.val)
            if node.right:
                adj_list[node.val].append(node.right.val)
                adj_list[node.right.val].append(node.val)
            graph_convert(node.left)
            graph_convert(node.right)
        
        graph_convert(root)

        q = deque()
        q.append((target.val,0))
        visit = set()
        res = []
        #print(adj_list)
        while q:
            node,dist = q.popleft()
            if dist == k:
                res.append(node)
            visit.add(node)
            for j in adj_list[node]:
                if j not in visit:
                    q.append((j,dist+1))
        return res

