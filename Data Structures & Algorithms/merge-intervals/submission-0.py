class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for interval in intervals[1:]:
            new_start, new_end = interval
            start, end = merged[-1]
            # ovverlaps
            if end >= new_start:
                if end > new_end:
                    merged[-1][-1] = end
                else:
                    merged[-1][-1] = new_end
            else:
                merged.append(interval)
            
        
        return merged


            