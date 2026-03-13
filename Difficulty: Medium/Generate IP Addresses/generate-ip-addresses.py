class Solution:
    def generateIp(self, s):
        n = len(s)
        ans = []
        
        # IP length must be between 4 and 12
        if n < 4 or n > 12:
            return []
        
        # Try all possible positions for 3 dots
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    
                    a = s[:i]
                    b = s[i:j]
                    c = s[j:k]
                    d = s[k:]
                    
                    # Check validity
                    if (self.valid(a) and self.valid(b) and 
                        self.valid(c) and self.valid(d)):
                        
                        ans.append(a + "." + b + "." + c + "." + d)
        
        return ans
    
    def valid(self, part):
        # No leading zero (except single 0)
        if len(part) > 1 and part[0] == '0':
            return False
        
        # Must be <= 255
        if int(part) > 255:
            return False
        
        return True