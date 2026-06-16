from heapq import heapify, heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}

        for num in nums:
            if num in vals:
                vals[num] += 1
            else:
                vals[num] = 1
        
        ans = []
        heapify(ans)

        for key, val in vals.items():
            heappush(ans, (val, key))
            if len(ans) > k:
                heappop(ans)
        
        res = []
        for val, key in ans:
            res.append(key)
        return res