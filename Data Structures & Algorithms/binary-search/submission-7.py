class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            index = int((l + r) / 2)
            sus = nums[index]

            if sus > target:
                r = index - 1
            elif sus < target:
                l = index + 1
            else:
                return index
            
        return -1