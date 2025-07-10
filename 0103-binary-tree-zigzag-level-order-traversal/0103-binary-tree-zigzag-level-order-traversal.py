# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        level = 0
        while q:
            level_res = deque()
            for i in range(len(q)):
                node = q.popleft()
                if level % 2 ==0:
                    level_res.append(node.val)
                else:
                    level_res.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level +=1
            res.append(list(level_res))
        return res



