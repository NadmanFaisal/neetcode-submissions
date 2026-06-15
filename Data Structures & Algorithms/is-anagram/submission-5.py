class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_one = {}
        map_two = {}

        for i in range(len(s)):
            char_one = s[i]
            if char_one not in map_one:
                map_one[char_one] = 1        
            else:
                map_one[char_one] += 1
        
            char_two = t[i]
            if char_two not in map_two:
                map_two[char_two] = 1
            else:
                map_two[char_two] += 1
                
        
        if map_one == map_two:
            return True
        else:
            return False