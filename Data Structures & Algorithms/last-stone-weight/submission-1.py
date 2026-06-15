class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-s for s in stones]
        heapq.heapify(weights)

        while len(weights) > 1:
            weight1 = heapq.heappop(weights)
            weight2 = heapq.heappop(weights)

            newWeight = weight1 - weight2

            if newWeight < 0:
                heapq.heappush(weights, newWeight)
        
        if weights:
            return abs(weights[0])
        else:
            return 0