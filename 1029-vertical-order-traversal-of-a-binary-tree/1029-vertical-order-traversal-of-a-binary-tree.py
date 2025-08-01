# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        nodes = collections.defaultdict(list)
        if not root:
            return []
        q.append([0,0,root])
        min1=max1=0
        while q:
            for i in range(len(q)):
                r,c,node = q.popleft()
                min1=min(min1,c)
                max1=max(max1,c)
                nodes[c].append((r,node.val))
                if node.left:
                    q.append([1+r,c-1,node.left])
                if node.right:
                    q.append([1+r,c+1,node.right])
        res = []
        
        
        for key in range(min1,max1+1):
            res.append([val for row, val in sorted(nodes[key])])
        return res