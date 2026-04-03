'''
for this problem same approach as leetcode_62 take the position into consideration add the paths
of the left and the top but there is a catch for the position where there is an obstacle keep 
the paths as 0 but for the ones where i == 0 or j == 0 1st column or 1st row we cannot reach the
positions after the obstacle so once an obstacle is detected in the first column or row we keep all
the paths for those positions to be 0.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[-1][-1]