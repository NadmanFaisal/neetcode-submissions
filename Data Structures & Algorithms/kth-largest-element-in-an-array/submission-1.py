class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        res = []
        heapq.heapify(res)
        
        while k > 0:
            value = heapq.heappop(max_heap)
            heapq.heappush(res, -value)
            k -= 1
        
        return res[0]