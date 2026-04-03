'''
Greedy approach so for this you need to take into consideration the nearest needed zeroes row from the current row
if we reach the end without finding the needed then return -1 when we reach the needed value we swap the zeroes values
of the rows until we reach the current. we do this until the end of execution.
'''

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vals = []
        for i in range(n):
            count = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] != 0:
                    break
                count+=1
            vals.append(count)
        swaps = 0
        for i in range(n):
            j = i
            needed = n - i - 1
            while j < n and vals[j] < needed:
                j+=1
            if j == n:
                return -1
            while j > i:
                vals[j], vals[j-1] = vals[j-1],vals[j]
                j-=1
                swaps += 1
        return swaps