class Solution:    
    def findUnion(self, a, b):
        # code here
        set_a=set(a)
        set_b=set(b)
        result=set_a.union(set_b)
        return list(result)