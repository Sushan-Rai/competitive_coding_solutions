'''
for this problem we need to take into consideration the position which we want to use
and get the max for that position we can start of with the first element which will give
us the first element itself to steal for the second it will be the 2nd element itself
if we want to include it and steal for the 3rd element we have only one option that is
to add the first element to the 3rd element this way we can propose a dp solution where
in the max we can steal for that particular position is adding it with the max of the
positions i-2 and i-3 since these will record the previous additions in place.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = nums[:]
        dp[2] += dp[0]
        for i in range(3,len(nums)):
            dp[i] = nums[i] + max(dp[i-2],dp[i-3])
        return max(dp[-1],dp[-2])