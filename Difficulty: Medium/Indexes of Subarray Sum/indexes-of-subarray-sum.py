#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        l = 0
        current_sum = 0
        for r in range(len(arr)):
            current_sum += arr[r]
            while current_sum > target and l <= r:
                current_sum -= arr[l]
                l += 1
            if current_sum == target:
                return [l + 1, r + 1]
        return [-1]
