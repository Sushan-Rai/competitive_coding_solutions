'''
for this problem we need to find a path from source top left to the bottom right with only
movements being right and bottom so for this we will add up the values for the first column
and the first row since theres only one path and for every position we take the sum of the 
current element and the minimum of the top path and the left path. this way we get minimum 
for that particular path then we can return the bottom right path for that particular matrix.
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [grid[i][:] for i in range(m)]
        for i in range(1,n):
            grid[0][i] += grid[0][i-1]
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]