class Solution:
    def largestSwap(self, s):
        s = list(s)
        last = {}

        # store last occurrence of each digit
        for i in range(len(s)):
            last[s[i]] = i

        # try swapping
        for i in range(len(s)):
            for d in range(9, int(s[i]), -1):
                if str(d) in last and last[str(d)] > i:
                    j = last[str(d)]
                    s[i], s[j] = s[j], s[i]
                    return "".join(s)

        return "".join(s)