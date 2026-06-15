class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lP = 0
        res = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[lP])
                lP += 1
            char_set.add(s[r])
            res = max(res, r - lP + 1)
        return res


        