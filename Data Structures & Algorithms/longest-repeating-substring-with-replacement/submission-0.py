class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = 0
        l = 0
        res = 0
        count = {}

        while r < len(s):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res

