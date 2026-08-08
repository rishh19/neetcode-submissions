class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_end=nums[0]
        min_end=nums[0]
        max_prod = nums[0]

        for i in range(1,len(nums)):
            v1=nums[i]
            v2=max_end * nums[i]
            v3=min_end * nums[i]

            min_end=min(v1,v2,v3)
            max_end=max(v1,v2,v3)

            max_prod = max(max_prod,max(v1,v2,v3))

        return max_prod