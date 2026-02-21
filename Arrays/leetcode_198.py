'''
so generally modifying the input is not recommended but i did this to effeciently
solve the problem could use a dp array and populate the results.
then used the max resultof the nums in the previous places since the array elements were 
positive there cannot be a gap of more than 2 elements to get maximum result.
and the result could be last or last second element since we can go alternate or 2 places
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3,len(nums)):
            nums[i] += max(nums[i-3],nums[i-2])
        return max(nums[-2],nums[-1])