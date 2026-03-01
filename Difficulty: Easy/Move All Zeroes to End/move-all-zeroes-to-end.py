class Solution:
    def pushZerosToEnd(self, arr):
        count = 0  
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        while count < len(arr):
            arr[count] = 0
            count += 1
        
        return arr