class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        wsum=0
        min_len =  float("inf")

        for h in range(len(nums)):
            wsum+= nums[h]
            while wsum >= target:
                min_len = min(min_len,h-l+1)
                wsum-=nums[l]
                l+=1

        if min_len == float("inf"):
            return 0
        return min_len