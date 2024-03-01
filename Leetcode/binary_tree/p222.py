class Solution:
    count = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root:
            self.count +=1
        self.countNodes(root.left)
        self.countNodes(root.right)
        return self.count