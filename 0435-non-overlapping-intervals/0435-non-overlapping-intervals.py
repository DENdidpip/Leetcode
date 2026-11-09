class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x:x[1])
        end = intervals[0][1]
        rem =0
        for i, j in intervals[1:]:
            if i < end:
                rem +=1
            else:
                end = j
        return rem
            
        