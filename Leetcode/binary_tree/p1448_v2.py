# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getPathToVal(root, path, count):
            if not root:
                return count
            else:
                path.append(root)
                if root.val==max([node.val for node in path]):
                    count += 1 
                leftCount = getPathToVal(root.left, path, count)
                rightCount = getPathToVal(root.right, path, leftCount)
                path.pop()
                return rightCount
        path = []
        count = 0
        res = getPathToVal(root, path, count)
        return res




        