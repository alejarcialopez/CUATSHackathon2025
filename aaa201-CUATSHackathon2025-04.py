# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root1, root2):
    if (root1 is None) and (root2 is None):
        return 1
    else:
        
        if (root1 is None) ^ (root2 is None):
            return 0

        if root1.val != root2.val:
            return 0
        

        return 1 * preorder(root1.left, root2.left) * preorder(root1.right, root2.right)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return bool(preorder(p,q))