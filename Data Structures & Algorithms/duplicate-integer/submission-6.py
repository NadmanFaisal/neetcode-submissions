class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for num in nums:
            vals.add(num)
        if len(vals) == len(nums):
            return False
        return True