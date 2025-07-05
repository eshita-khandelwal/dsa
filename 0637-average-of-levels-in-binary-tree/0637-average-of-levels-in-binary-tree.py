# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #use BFS here
        q = deque()
        q.append(root)
        res = []
        while q:
            level_length = len(q)
            sum1 = 0
            for i in range(level_length):
                node = q.popleft()
                sum1 +=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum1/level_length)
        return res