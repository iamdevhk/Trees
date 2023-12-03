import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        q=collections.deque()
        q.append(root)
        while q:
            right=None
            n=len(q)
            for i in range (n):
                node=q.popleft()
                if node:
                    right=node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                result.append(right.val) 
        return result