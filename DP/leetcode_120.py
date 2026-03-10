'''
for the problem we need to find the minimum total sum path from the start i.e top to the bottom
we can do this by adding the end most nodes since they have only one path to consider that is 
first and last element of every row and we can add the minimum of the upper 2 elements row and 
get the solution for that particular row. for the result we can just take the minimum of last 
row which will get us the path.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [triangle[i][:] for i in range(m)]
        for i in range(1,m):
            dp[i][0] += dp[i-1][0]
            dp[i][-1] += dp[i-1][-1]
        for i in range(1,m):
            for j in range(1,len(triangle[i])-1):
                dp[i][j] += min(dp[i-1][j],dp[i-1][j-1])
        return min(dp[-1])