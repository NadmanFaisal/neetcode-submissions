class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            value = heapq.heappop(minHeap)
            coord = [value[1], value[2]]
            res.append(coord)
            k -= 1
        
        return res