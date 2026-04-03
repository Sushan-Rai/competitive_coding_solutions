# Intuition and Approach
# First of all how would you know if this is a Digit DP look at the constraints its above 10**9 this clearly means digit dp is required but this one is not a classic case of digit dp since while traversing itself we require to keep checking the monotonicity lets break this into simple steps

# First try to build the digit dp check if the numbers are going from 0 to that number use tight to take reference and restrict the numbers to not exceed that digits place for example 123 is the number
# if the number starts from 1 in the hundreds place then it shouldnt exceed 2 in the tenths place and so on.
# then try to build the base case which is checking if the sum is monotone this we can first of all check the limits of how much a sum can reach upto worst case 9(15times) which is 9+9+... = 9*15 = 135 three digit which is not huge so while loop is fine.
# now build the monotone case for the numbers while traversal this needs states to check if the check is for increment or decrement and if the existing number is monotone at the time of traversal. another addition is leading zeroes since leading zeroes will cause a problem otherwise while checking for monotone giving us 0 results. inc can be 1, 0, -1 which is increment, decrement, none(initial or notGood)
# make this a solver and solve it for r and l-1
class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def solve(r):
            r_digits = []
            temp = r
            while temp > 0:
                r_digits.append(temp%10)
                temp = temp//10
            r_digits = r_digits[::-1]
            from functools import lru_cache
            @lru_cache(maxsize=None)
            def dp(pos, num,tight,sum_,inc, isGood, leadingzeroes):
                if pos == len(r_digits):
                    if(isGood):
                        return 1
                    arr = []
                    temp = sum_
                    while sum_ > 0:
                        arr.append(sum_%10)
                        sum_ = sum_//10
                    incr = 0
                    decr = 0
                    for i in range(1,len(arr)):
                        if arr[i] > arr[i-1]:
                            incr += 1
                        elif arr[i] < arr[i-1]:
                            decr += 1
                        else:
                            incr+=1
                            decr+=1
                    print(temp,incr,decr)
                    if incr == 0 or decr == 0:
                        return 1
                    return 0
                max_dig = 9 if tight is False else r_digits[pos]
                count = 0
                for i in range(max_dig+1):
                    new_tight = tight and i == max_dig
                    if leadingzeroes:
                        leading_new = leadingzeroes and (i==0)
                        count += dp(pos+1,i,new_tight,sum_+i,-1,True,leading_new)
                    elif isGood == False:
                        count += dp(pos+1,i,new_tight,sum_+i,-1,False,leadingzeroes)
                    else:
                        if inc == -1:
                            isNewGood = False
                            newInc = -1
                            if i > num%10:
                                isNewGood = True
                                newInc = 1
                            elif i < num%10:
                                isNewGood = True
                                newInc = 0
                            count+=dp(pos+1,i,new_tight,sum_+i,newInc, isNewGood, leadingzeroes)
                        elif inc == 1:
                            ref = i > num%10
                            if ref == True:
                                count+=dp(pos+1,i,new_tight,sum_+i,1,isGood,leadingzeroes)
                            else:
                                count+=dp(pos+1,i,new_tight,sum_+i,-1,False,leadingzeroes)
                        else:
                            ref = i < num%10
                            if ref == True:
                                count+=dp(pos+1,i,new_tight,sum_+i,0,isGood,leadingzeroes)
                            else:
                                count+=dp(pos+1,i,new_tight,sum_+i,-1,False,leadingzeroes)
                return count
            return dp(0,0,True,0,-1,True,True)
        return solve(r) - solve(l-1)