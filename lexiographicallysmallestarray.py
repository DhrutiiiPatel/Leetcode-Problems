class Solution(object):
    def longestZigZag(self, root):       
        def dfs(node, direction, length):
            if not node:
                return length - 1  
            if direction == "left":
                return max(
                    dfs(node.left, "right", length + 1),
                    dfs(node.right, "left", 1)
                )
            else:  
                return max(
                    dfs(node.right, "left", length + 1),
                    dfs(node.left, "right", 1)
                )
        if not root:
            return 0
        return max(
            dfs(root.left, "right", 1),
            dfs(root.right, "left", 1)
        )
