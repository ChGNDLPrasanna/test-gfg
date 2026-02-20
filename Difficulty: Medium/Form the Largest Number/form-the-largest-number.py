class Solution:
    def findLargest(self, arr):
        arr=list(map(str,arr))
        from functools import cmp_to_key
        def compare(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0
        arr.sort(key=cmp_to_key(compare))
        result=''.join(arr)
        if result[0]=='0':
            return "0"
        return result