class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # If there are no intervals
        if len(intervals) == 0:
            return True

        # Sort by starting time
        intervals.sort(key=lambda x: x.start)

        # Take the first interval
        start1 = intervals[0].start
        end1 = intervals[0].end

        for i in range(1, len(intervals)):

            # Take the next interval
            start2 = intervals[i].start
            end2 = intervals[i].end

            # Check overlap
            if end1 > start2:
                return False

            # Move to the next interval
            start1 = start2
            end1 = end2

        return True