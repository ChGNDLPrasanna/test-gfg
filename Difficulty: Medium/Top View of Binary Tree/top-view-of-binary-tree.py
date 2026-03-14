'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        
        if root is None:
            return []
        
        q = deque([(root, 0)])   # (node, horizontal distance)
        mp = {}                  # store first node at each distance
        
        while q:
            node, hd = q.popleft()
            
            if hd not in mp:     # first node seen at this distance
                mp[hd] = node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        ans = []
        for i in sorted(mp):
            ans.append(mp[i])
        
        return ans