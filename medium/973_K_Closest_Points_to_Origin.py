class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        size = 0
        heap = []
        for (x, y) in points:
            distance = -(x**2 + y**2)
            if size < k:
                heapq.heappush(heap, (distance, x, y))
            else:
                heapq.heappushpop(heap, (distance, x, y))
            size+=1
        return [(x,y) for (dist,x, y) in heap]
        
