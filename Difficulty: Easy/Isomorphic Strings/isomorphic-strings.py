class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        m1 = {}
        m2 = {}
        
        for a, b in zip(s1, s2):
            if a in m1:
                if m1[a] != b:
                    return False
            else:
                if b in m2:
                    return False
                m1[a] = b
                m2[b] = a
        
        return True