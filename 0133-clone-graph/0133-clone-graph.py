"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashMap = {} #old-> new
        def dfs(node):
            if node in hashMap:
                return hashMap[node]
            copyNode = Node(node.val)
            hashMap[node] = copyNode

            for nei in node.neighbors:
                copyNode.neighbors.append(dfs(nei))
            return copyNode
        
        return dfs(node)
