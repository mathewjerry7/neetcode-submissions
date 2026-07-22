class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newlist = []
        i=0
        n= len(intervals)

        while i<n and newInterval[0] > intervals[i][1]:
            newlist.append(intervals[i])
            i += 1

        # now here since newInterval[0] > intervals[i][1]
        # it already exited the above loop means newInterval[0] <= intervals[i][1]
        # so we add the second condition as well which is newInterval[1] >= intervals[i][0]
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i += 1
        
        newlist.append(newInterval)

        while i<n:
            newlist.append(intervals[i])
            i += 1

        return newlist

