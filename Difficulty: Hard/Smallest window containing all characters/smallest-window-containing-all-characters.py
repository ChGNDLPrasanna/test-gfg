class Solution:
    def minWindow(self, s, p):
        from collections import Counter
        
        need = Counter(p)
        missing = len(p)
        left = start = end = 0
        
        for right in range(len(s)):
            
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1
            
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if end == 0 or right-left+1 < end-start:
                    start, end = left, right+1
                
                need[s[left]] += 1
                missing += 1
                left += 1
        
        return s[start:end]