'''
Dont overcomplicate things, since we compare the strings just make the comparison of string i
and string j and then swap it, this is a custom sort. so therefore we get the result.
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        # s = "abc"
        # rep = 5//len(s) + 1
        # print(("abc"*rep)[:5])
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                str_i = str(nums[i])
                str_j = str(nums[j])
                if int(str_i+str_j) > int(str_j+str_i):
                    nums[i],nums[j] = nums[j],nums[i]
                # len_i = len(str(nums[i]))
                # len_j = len(str(nums[j])) 
                # req_length = max(len_i,len_j)
                # avai_length = min(len_i,len_j)
                # rep = req_length//avai_length + 1
                # if len_i == len_j:
                #     nums[i], nums[j] = min(nums[i],nums[j]),max(nums[i],nums[j])
                # elif len_i < len_j:
                #     val_i = int((str(nums[i])*rep)[:req_length])
                #     val_j = nums[j]
                #     if val_i >= val_j:
                #         nums[i],nums[j] = nums[j],nums[i]
                # else:
                #     val_j = int((str(nums[j])*rep)[:req_length])
                #     val_i = nums[i]
                #     if val_i >= val_j:
                #         nums[i],nums[j] = nums[j],nums[i]
        res = ""
        for i in range(len(nums)-1,-1,-1):
            res+=str(nums[i])
        if int(res) == 0:
            return "0"
        return res
