class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])

        res = []
        res.append(intervals[0])

        for start, end in intervals:
            latest_interval = res[-1]
            if start <= latest_interval[1]:
                greater_end = max(end, latest_interval[1])
                latest_interval[1] = greater_end
            else:
                res.append([start,end])
                
        return res
        