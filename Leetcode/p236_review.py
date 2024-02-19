# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#borrowed Marlen09
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root 

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root 
            
        return l or r

#mycode
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getPathFromRoot(root, targetNode): #get path from root to a node with value
            def dfs(root, targetNode, path):
                if not root: #at a NULL node
                    return   #simply go back
                else:
                    path.append(root)
                    if root.val == targetNode.val: #stop dfs here 
                        return path
                    dfs(root.left, targetNode, path)
                    dfs(root.right, targetNode, path)
                    path.pop()
            path = []
            dfs(root, targetNode, path)
            return path
        path1 = getPathFromRoot(root, p)
        path2 = getPathFromRoot(root, q)

        print(len(path1))
        print(len(path2))

        maxLen = min(len(path1), len(path2))
        i=0
        while (i<maxLen):
            if path1[i].val!=path2[i].val:
                break
            i+=1
        return path1[i-1]


        
        