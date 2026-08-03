class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxcount=0

        for number in nums:
            if number==1:
                count+=1
            else:
                count=0
            maxcount=max(maxcount,count)
        return maxcount