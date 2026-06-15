class Solution:
    def isPalindrome(self, s: str) -> bool:
        lP = 0
        rP = len(s) - 1

        while lP < rP:
            if not s[lP].isalnum():
                lP += 1
            elif not s[rP].isalnum():
                rP -= 1
            elif s[lP].lower() != s[rP].lower():
                return False
            else:
                rP -= 1
                lP += 1
        return True