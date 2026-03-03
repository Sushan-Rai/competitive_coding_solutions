'''
so for this problem we split the strings into hours and mins and then we sort them
once we sort them based on hours and then by minutes (if hours equal), we compare
the ith element with i+1th element and subtract the hours and mins but theres one
edge case wherein the element in the start has to be compared with the last element
of the hour_mins array from the reverse.
'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        hour_mins = [list(map(int,i.split(":"))) for i in timePoints]
        # print(hour_mins)
        hour_mins = sorted(hour_mins, key= lambda x: [x[0],x[1]])
        # print(hours)
        res = float('inf')
        for i in range(len(hour_mins)-1):
            j = i + 1
            if hour_mins[i][0] > hour_mins[j][0]:
                greater = hour_mins[i]
                lesser = hour_mins[j]
            elif hour_mins[i][0] < hour_mins[j][0]:
                greater = hour_mins[j]
                lesser = hour_mins[i]
            else:
                if hour_mins[i][1] < hour_mins[j][1]:
                    greater = hour_mins[j]
                    lesser = hour_mins[i]
                else:
                    greater = hour_mins[i]
                    lesser = hour_mins[j]
            ans1 = (greater[0] - lesser[0]) * 60  + (greater[1] - lesser[1])
            # ans2 = (23 - greater[0]) * 60 + (lesser[0]) * 60 + (60 - greater[1]) + lesser[1]
            res = min(res, ans1)
        ans2 = (23 - hour_mins[-1][0]) * 60 + (hour_mins[0][0]) * 60 + (60 - hour_mins[-1][1]) + hour_mins[0][1]
        res = min(res, ans2)
        return res

        