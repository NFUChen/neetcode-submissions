"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        seen = set()

        for interval in intervals:
            start = interval.start
            end = interval.end
            interval_range = range(start, end)
            for idx in interval_range:
                if idx in seen:
                    return False
            seen.update(interval_range)


        return True
