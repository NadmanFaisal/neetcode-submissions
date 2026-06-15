class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            current_product = 1
            for j in range(0, len(nums)):
                if j != i:
                    current_product *= nums[j]
            output.append(current_product)
        return output

    