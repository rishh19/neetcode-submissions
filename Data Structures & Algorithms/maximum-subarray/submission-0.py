class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_end = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            v1=nums[i]+best_end
            v2=nums[i]

            best_end=max(v1,v2)
            max_sum=max(max_sum,best_end)
        return max_sum