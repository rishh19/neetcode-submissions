class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        ans=0

        while l<=h:
            #find mid
            mid=l+(h-l)//2

            if mid * mid == x:
                return mid
            #store into ans & go right if mid * mid is lower than x
            elif mid * mid < x:
                ans=mid #best answer is stored till now
                l=mid+1
            else:
                h=mid-1
        return ans