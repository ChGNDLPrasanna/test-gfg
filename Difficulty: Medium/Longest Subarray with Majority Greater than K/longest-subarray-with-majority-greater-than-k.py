class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        prefix = 0
        max_len = 0
        first = {}

        for i in range(len(arr)):
       
            if arr[i] > k:
                prefix += 1
            else:
                prefix -= 1  
            if prefix > 0:
                max_len = i + 1
            else:
                
                if prefix not in first:
                    first[prefix] = i

                
                if (prefix - 1) in first:
                    length = i - first[prefix - 1]
                    max_len = max(max_len, length)

        return max_len