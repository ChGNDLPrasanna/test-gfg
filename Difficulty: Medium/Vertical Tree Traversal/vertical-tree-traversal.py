'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        # code here
        if not root:
            return []
        
        mp = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            mp[hd].append(node.data)
            
            if node.left:
                q.append((node.left, hd-1))
            if node.right:
                q.append((node.right, hd+1))
        
        res = []
        for k in sorted(mp):
            res.append(mp[k])
        
        return res