class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        lmax=height[l]
        rmax=height[r]
        water=0

        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,height[l])
                water=water+lmax-height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                water=water+rmax-height[r]
        return water
        