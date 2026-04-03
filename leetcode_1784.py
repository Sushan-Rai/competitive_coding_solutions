'''
So for this problem its relatively simple u just need to find the segments of 1
the segments of 1 is a continous stream of 1 it could be of length from 1 to n
counting these segments is the key u can keep track of the segments by a previous element
or through traversal till the n-1th element.
'''

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        prev = 0
        for i in s:
            if prev == 0 and i == "1":
                count+=1
                prev = 1
            elif i == "1":
                prev = 1
            else:
                prev = 0
        return count <= 1