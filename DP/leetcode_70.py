'''
pretty simple to get to the solution so for this imagine you are in a particular position lets say x
how would you reach that position with the possiblities being 1 step and 2 steps to reach x you would 
need to jump from x-1th position or x-2th position, what would you need for the x-2th position similar
stuff, you need to backtrack until u reach 1 and 2 and we can already deduce that 1st position has a 
possiblity of 1 and 2nd position has a possiblity of 2. Therefore for any x position = possiblities of
x-1 + possiblities of x-2 should give you the result.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        n1 = 1
        n2 = 2
        i = 2
        while i < n:
            t = n2
            n2 = n1 + n2
            n1 = t
            i+=1
        return n2