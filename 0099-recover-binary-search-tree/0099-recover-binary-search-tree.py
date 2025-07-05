# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #get the inorder traversal

        first,middle,last  = None,None,None
        prev = None
        def inorder(root):
            nonlocal first,middle,last,prev
            if not root:
                return
            inorder(root.left)
            #lets do the assignment here
            if prev is not None and prev.val > root.val:
                if first is None:
                    first = prev
                    middle = root
                else:
                    last = root
            prev = root
            inorder(root.right)
        inorder(root)
        print(last)
        #just swap the values here swaping nodes is not required
        if first and last:
            first.val, last.val = last.val, first.val
        elif first and middle:
            first.val, middle.val = middle.val, first.val

        return root
