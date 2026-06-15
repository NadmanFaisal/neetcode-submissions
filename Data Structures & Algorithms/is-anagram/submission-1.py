class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        val1 = {}
        val2 = {}

        for i in range(0, len(s)):
            if s[i] in val1:
                val1[s[i]] += 1
            else:
                val1[s[i]] = 0

            if t[i] in val2:
                val2[t[i]] += 1
            else:
                val2[t[i]] = 0

        for key in val1.keys():
            if key not in val1:
                return False
            if key not in val2:
                return False

            if val1[key] != val2[key]:
                return False

        return True


        