class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flip = [0] * n
        curr_flip = 0
        ans = 0

        for i in range(n):
            
            if i >= k:
                curr_flip ^= flip[i - k]

            if arr[i] ^ curr_flip == 0:
                if i + k > n:
                    return -1

                ans += 1
                curr_flip ^= 1
                flip[i] = 1

        return ans