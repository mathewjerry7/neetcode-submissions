from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        sorted_nums = sorted(count, key=lambda x: count[x], reverse=True)
        
        return sorted_nums[:k]

#Heap Method
        # count = {}
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # heap = [(-c, n) for n, c in count.items()]
        # heapq.heapify(heap)

        # return [heapq.heappop(heap)[1] for _ in range(k)]

