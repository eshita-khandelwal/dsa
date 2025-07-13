class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        end1 = 0
        for start,end in intervals:
            if start < end1 or end <end1:
                return False
            end1 = max(end1,end)
        return True
