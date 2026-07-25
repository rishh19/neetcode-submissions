class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        maxA=0

        while l<r:
            h=min(height[l],height[r])
            w=r-l
            A=h*w
            maxA=max(maxA,A)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxA
        