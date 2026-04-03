'''
This problem i had a tough time solving so basically the approach is to
use start array to keep track of whether the last element has the 
sum compounding from the start and we do this in reverse and take the max
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            return max(nums)
        if len(nums) == 4:
            return max(nums[0]+nums[2], nums[1]+nums[3])
        dp = [0] * len(nums)
        dp[0],dp[1],dp[2] = nums[0],nums[1],nums[0]+nums[2]
        start = [False] * len(nums)
        start[0],start[1],start[2] = True,False,True
        for i in range(3, len(nums)):
            if dp[i-2] >= dp[i-3]:
                start[i] = start[i-2]
            else:
                start[i] = start[i-3]
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
        if start[-1] == True:
            max_ = max(dp[-2],dp[-3])
        else:
            max_ = max(dp[-1],dp[-2])
        nums = nums[::-1]
        dp = [0] * len(nums)
        dp[0],dp[1],dp[2] = nums[0],nums[1],nums[0]+nums[2]
        start = [False] * len(nums)
        start[0],start[1],start[2] = True,False,True
        for i in range(3, len(nums)):
            if dp[i-2] >= dp[i-3]:
                start[i] = start[i-2]
            else:
                start[i] = start[i-3]
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
        if start[-1] == True:
            max__ = max(dp[-2],dp[-3])
        else:
            max__ = max(dp[-1],dp[-2])
        return max(max_,max__)