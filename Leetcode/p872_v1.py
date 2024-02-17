# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafList(root, curr, lst):
            if not curr:
                return lst
            if not curr.left and not curr.right:
                lst.append(curr.val)
                return lst
            getLeafList(root, curr.left, lst)
            getLeafList(root, curr.right, lst)
            if curr == root:
                return lst
        return getLeafList(root1, root1, [])==getLeafList(root2, root2, [])