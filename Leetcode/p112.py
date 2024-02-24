class Solution:
    pathFound = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return bool(0)

            if self.pathFound==1:
                return bool(1)

            currSum += node.val #5 9 20 22

            if not node.left and not node.right:
                if currSum==targetSum:
                    self.pathFound=1
                    return bool(1)

            return dfs(node.left, currSum) or dfs(node.right, currSum)
        
        dfs(root, 0)
        return bool(self.pathFound)