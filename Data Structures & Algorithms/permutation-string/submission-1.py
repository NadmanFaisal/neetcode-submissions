class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = {}
        for char in s1:
            if char in count_s1:
                count_s1[char] += 1
            else:
                count_s1[char] = 1
        count_s2 = {}
        for l in range(len(s2) - len(s1) + 1):
            for r in range(l, l + len(s1)):
                if s2[r] in count_s2:
                    count_s2[s2[r]] += 1
                else:
                    count_s2[s2[r]] = 1

                if count_s2 == count_s1:
                    return True
            count_s2 = {}
        
        return False
