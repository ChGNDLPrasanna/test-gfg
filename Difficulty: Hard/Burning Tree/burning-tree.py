'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        # code here
          # Step 1: Store parent mapping
        parent = {}
        target_node = None
        
        def mark_parent(node, par):
            nonlocal target_node
            if not node:
                return
            
            if node.data == target:
                target_node = node
            
            parent[node] = par
            
            mark_parent(node.left, node)
            mark_parent(node.right, node)
        
        mark_parent(root, None)
        
        # Step 2: BFS for burning
        q = deque()
        visited = set()
        
        q.append(target_node)
        visited.add(target_node)
        
        time = 0
        
        while q:
            size = len(q)
            burned = False
            
            for _ in range(size):
                node = q.popleft()
                
                # left child
                if node.left and node.left not in visited:
                    burned = True
                    visited.add(node.left)
                    q.append(node.left)
                
                # right child
                if node.right and node.right not in visited:
                    burned = True
                    visited.add(node.right)
                    q.append(node.right)
                
                # parent
                if parent[node] and parent[node] not in visited:
                    burned = True
                    visited.add(parent[node])
                    q.append(parent[node])
            
            if burned:
                time += 1
        
        return time