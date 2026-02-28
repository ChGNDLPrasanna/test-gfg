class Solution:
    def findClosestPair(self, arr1, arr2, x):
        i = 0                  # start of arr1
        j = len(arr2) - 1      # end of arr2
        min_diff = float('inf')
        pair = [0, 0]

        while i < len(arr1) and j >= 0:
            current_sum = arr1[i] + arr2[j]
            diff = abs(current_sum - x)

            if diff < min_diff:
                min_diff = diff
                pair = [arr1[i], arr2[j]]

            if current_sum < x:
                i += 1
            else:
                j -= 1

        return pair