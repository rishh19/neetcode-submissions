class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        n=len(nums)
        for fast in range(0,n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow+=1
        
        while slow < n:
            nums[slow] = 0
            slow+=1