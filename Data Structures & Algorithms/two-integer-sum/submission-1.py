class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(0, len(nums)):
            suspect = target - nums[i]
            if suspect in hash_map:
                return [hash_map[suspect], i]
            else:
                hash_map[nums[i]] = i

        