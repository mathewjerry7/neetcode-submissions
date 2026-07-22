class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by start time, since input is not guaranteed sorted
        intervals.sort(key= lambda x: x[0])
        
        result = []

        for interval in intervals:
            
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            
            else:
                # overlap, stretch the end of the last one
                result[-1][1] = max(result[-1][1],interval[1])

        return result