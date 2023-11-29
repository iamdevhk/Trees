class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            nonlocal ans
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            ans = max(ans, lh + rh)
            return 1 + max(lh, rh)
        
        ans = 0
        s=height(root)
        return ans