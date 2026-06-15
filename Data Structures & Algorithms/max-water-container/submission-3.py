class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lP = 0
        rP = len(heights) - 1
        
        leftHeight = heights[lP]
        rightHeight = heights[rP]
    
        maxArea = 0
    
        while lP < rP:
            area = (rP - lP ) * min(heights[lP], heights[rP])
            if area > maxArea:
                maxArea = area
    
            if heights[lP] < heights[rP]:
                lP += 1
            else:
                rP -= 1
        return maxArea
