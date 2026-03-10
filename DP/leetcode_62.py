'''
for this problem we can compute the paths being taken for each grid starting from the start grid
we notice a pattern that once we reach a point there can be only 2 places it can be reached from
either the top or from the left if we have computed the total number of paths for top and the 
left then the spot we are aiming for will be the sum of paths of left and top.
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]