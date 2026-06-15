class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        min_heap = []
        for key, val in hash_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key))
            else:
                heapq.heappushpop(min_heap, (val, key))

        res = []
        for val in min_heap:
            res.append(val[1])
        return res


        