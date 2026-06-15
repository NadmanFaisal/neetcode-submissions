class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lP = 0
        rP = len(numbers) - 1
        while (lP <= rP):
            sum = numbers[lP] + numbers[rP]
            if sum > target:
                rP -= 1
            elif sum < target:
                lP += 1
            else:
                return [lP + 1, rP + 1]


